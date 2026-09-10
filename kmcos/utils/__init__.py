#!/usr/bin/env python3
"""Several utility functions that do not seem to fit somewhere
   else.
"""
#    Copyright 2009-2013 Max J. Hoffmann (mjhoffmann@gmail.com)
#    This file is part of kmcos.
#
#    kmcos is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    kmcos is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with kmcos.  If not, see <http://www.gnu.org/licenses/>.
from __future__ import with_statement
from __future__ import print_function
import os
import re
import shutil
from time import time
from io import StringIO
from kmcos.utils.ordered_dict import OrderedDict

ValidationError = UserWarning
try:
    from kiwi.datatypes import ValidationError
except:
    print('Warning: kiwi Validation not working. (this warning is expected)' )

#NB The kind values used to be obtained by building a small Fortran module
#NB (FCODE) through numpy.f2py.compile and importing it. That function was
#NB deprecated in NumPy 1.26 and removed in 2.0, so the same values are now
#NB obtained by compiling and running a standalone probe program directly
#NB with the Fortran compiler. No f2py involvement is needed for this.
KIND_PROBE_FCODE = """program kind_probe
  print '(I0)', {expression}
end program kind_probe
"""

#NB f2py/distutils compiler names mapped onto the actual executable, needed
#NB now that the compiler is invoked directly rather than through distutils.
FCOMPILER_EXECUTABLES = {
    'gnu95': 'gfortran',
    'gfortran': 'gfortran',
    'intel': 'ifort',
    'intelem': 'ifort',
    'ifort': 'ifort',
}


def fcompiler_executable(fcompiler=None):
    """Return the Fortran compiler executable to invoke directly."""
    if fcompiler is None:
        fcompiler = os.environ.get('F2PY_FCOMPILER', 'gfortran')
    return FCOMPILER_EXECUTABLES.get(fcompiler, fcompiler)


_KIND_CACHE = {}


def evaluate_fortran_kind(kind_type, args, kwargs):
    """Evaluate selected_real_kind/selected_int_kind by compiling and running
    a one-line Fortran program with the same compiler that builds the model.

    The argument handling reproduces the old FCODE module exactly, including
    its quirk that selected_int_kind ignores r whenever p is given.

    """
    import subprocess
    import tempfile

    p = kwargs.get('p')
    r = kwargs.get('r')
    #NB positional arguments were passed to the FCODE wrappers as (p, r)
    if len(args) > 0 and p is None:
        p = args[0]
    if len(args) > 1 and r is None:
        r = args[1]

    if kind_type == 'real':
        if p is not None and r is not None:
            expression = 'selected_real_kind(p=%s, r=%s)' % (p, r)
        elif r is not None:
            expression = 'selected_real_kind(r=%s)' % r
        else:
            expression = 'selected_real_kind(%s)' % p
    else:
        if p is not None:
            expression = 'selected_int_kind(%s)' % p
        else:
            expression = 'selected_int_kind(r=%s)' % r

    if expression in _KIND_CACHE:
        return _KIND_CACHE[expression]

    compiler = fcompiler_executable()
    tmpdir = tempfile.mkdtemp()
    try:
        source = os.path.join(tmpdir, 'kind_probe.f90')
        binary = os.path.join(tmpdir, 'kind_probe')
        with open(source, 'w') as outfile:
            outfile.write(KIND_PROBE_FCODE.format(expression=expression))
        try:
            subprocess.check_call([compiler, '-o', binary, source])
            output = subprocess.check_output([binary])
        except (OSError, subprocess.CalledProcessError) as e:
            raise Exception('Could not evaluate %s using %s\n%s'
                            % (expression, compiler, e))
        kind_value = int(output.strip())
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)

    _KIND_CACHE[expression] = kind_value
    return kind_value


class CorrectlyNamed:

    """Syntactic Sugar class for use with kiwi, that makes sure that the name
    field of the class has a name field, that always complys with the rules
    for variables.
    """

    def __init__(self):
        pass

    def on_name__validate(self, _, name):
        """Called by kiwi upon chaning a string
        """
        if ' ' in name:
            return ValidationError('No spaces allowed')
        elif name and not name[0].isalpha():
            return ValidationError('Need to start with a letter')


def write_py(fileobj, images, **kwargs):
    """Write a ASE atoms construction string for `images`
       into `fileobj`.
    """
    import numpy as np

    if isinstance(fileobj, str):
        fileobj = open(fileobj, 'w')

    scaled_positions = kwargs['scaled_positions'] \
        if 'scaled_positions' in kwargs else True
    fileobj.write('from ase import Atoms\n\n')
    fileobj.write('import numpy as np\n\n')

    if not isinstance(images, (list, tuple)):
        images = [images]
    fileobj.write('images = [\n')

    for image in images:
        if hasattr(image, 'get_chemical_formula'):
            chemical_formula = image.get_chemical_formula(mode='reduce')
        else:
            chemical_formula = image.get_name()
        cell_string = repr(image.cell)
        cell_string = cell_string.replace('cell', '')
        cell_string = cell_string.replace('Cell', '')
        fileobj.write("    Atoms(symbols='%s',\n"
                      "          pbc=np.%s,\n"
                      "          cell=np.array(      %s),\n" % (
                          chemical_formula,
                          repr(image.pbc),
                          cell_string))

        if not scaled_positions:
            fileobj.write("          positions=np.array(      %s),\n"
                          % repr(list(image.positions)))
        else:
            fileobj.write("          scaled_positions=np.array(      %s),\n"
                          % repr(list((np.around(image.get_scaled_positions(), decimals=7)).tolist())))
        #print(image.get_scaled_positions())
        fileobj.write('),\n')

    fileobj.write(']')


def get_ase_constructor(atoms):
    """Return the ASE constructor string for `atoms`."""
    if isinstance(atoms, str):
        #return atoms
        atoms = eval(atoms)
    if type(atoms) is type([]):
        atoms = atoms[0]
    f = StringIO()
    write_py(f, atoms)
    f.seek(0)
    lines = f.readlines()
    f.close()
    astr = ''
    for i, line in enumerate(lines):
        if i >= 5 and i < len(lines) - 1:
            astr += line
    # astr = astr[:-2]
    return astr.strip()


def product(*args, **kwds):
    """Take two lists and return iterator producing
    all combinations of tuples between elements
    of the two lists."""
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = [tuple(arg) for arg in args] * kwds.get('repeat', 1)
    result = [[]]
    for pool in pools:
        result = [x + [y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)


def split_sequence(seq, size):
    """Take a list and a number n and return list
       divided into n sublists of roughly equal size.
    """
    newseq = []
    splitsize = 1.0 / size * len(seq)
    for i in range(size):
        newseq.append(seq[int(round(i * splitsize)):
                      int(round((i + 1) * splitsize))])
    return newseq


def download(project):
    from django.http import HttpResponse
    import zipfile
    import tempfile
    from os.path import join, basename
    from glob import glob
    from kmcos.io import import_xml, export_source

    # return HTTP download response (e.g. via django)
    response = HttpResponse(mimetype='application/x-zip-compressed')
    response['Content-Disposition'] = 'attachment; filename="kmcos_export.zip"'

    if isinstance(project, str):
        project = import_xml(project)

    from io import StringIO
    stringio = StringIO()
    zfile = zipfile.ZipFile(stringio, 'w')

    # save XML
    zfile.writestr('project.xml', str(project))

    # generate source
    tempdir = tempfile.mkdtemp()
    srcdir = join(tempdir, 'src')

    # add kMC project sources
    export_source(project, srcdir)
    for srcfile in glob(join(srcdir, '*')):
        zfile.write(srcfile, join('src', basename(srcfile)))

    # add standalone kmcos program
    # TODO

    # write temporary file to response
    zfile.close()
    stringio.flush()
    response.write(stringio.getvalue())
    stringio.close()
    return response


def evaluate_kind_values(infile, outfile):
    """Go through a given file and dynamically
    replace all selected_int/real_kind calls
    with the dynamically evaluated fortran code
    using only code that the function itself
    contains.

    """
    import re

    with open(infile) as infh:
        intext = infh.read()
    if not ('selected_int_kind' in intext.lower()
            or 'selected_real_kind' in intext.lower()):
        shutil.copy(infile, outfile)
        return

    def parse_args(args):
        """
            Parse the arguments for selected_(real/int)_kind
            to pass them on to the Fortran module.

        """
        in_args = [x.strip() for x in args.split(',')]
        args = []
        kwargs = {}

        for arg in in_args:
            if '=' in arg:
                symbol, value = arg.split('=')
                kwargs[symbol] = eval(value)
            else:
                args.append(eval(arg))

        return args, kwargs

    def int_kind(args):
        """Python wrapper around Fortran selected_int_kind
        function.
        """
        args, kwargs = parse_args(args)
        return evaluate_fortran_kind('int', args, kwargs)

    def real_kind(args):
        """Python wrapper around Fortran selected_real_kind
        function.
        """
        args, kwargs = parse_args(args)
        return evaluate_fortran_kind('real', args, kwargs)

    infile = open(infile)
    outfile = open(outfile, 'w')
    int_pattern = re.compile((r'(?P<before>.*)selected_int_kind'
                              '\((?P<args>.*)\)(?P<after>.*)'),
                             flags=re.IGNORECASE)
    real_pattern = re.compile((r'(?P<before>.*)selected_real_kind'
                               '\((?P<args>.*)\)(?P<after>.*)'),
                              flags=re.IGNORECASE)

    for line in infile:
        real_match = real_pattern.match(line)
        int_match = int_pattern.match(line)
        if int_match:
            match = int_match.groupdict()
            line = '%s%s%s\n' % (
                match['before'],
                int_kind(match['args']),
                match['after'],)
        elif real_match:
            match = real_match.groupdict()
            line = '%s%s%s\n' % (
                match['before'],
                real_kind(match['args']),
                match['after'],)
        outfile.write(line)
    infile.close()
    outfile.close()


def build(options):
    """Build binary with f2py binding from complete
    set of source file in the current directory.

    """

    from os.path import isfile
    import os
    import sys
    from glob import glob

    src_files = ['kind_values_f2py.f90', 'base.f90']
    
    if isfile('base_acf.f90'):
        src_files.append('base_acf.f90')
    src_files.append('lattice.f90')
    if isfile('proclist_constants.f90'):
        src_files.append('proclist_constants.f90')
    if isfile('proclist_pars.f90'):
        src_files.append('proclist_pars.f90')

    src_files.extend(glob('nli_*.f90'))
    # src_files.extend(glob('get_rate_*.f90'))
    src_files.extend(glob('run_proc_*.f90'))
    src_files.append('proclist.f90')
    if isfile('proclist_acf.f90'):
        src_files.append('proclist_acf.f90')

    extra_flags = {}

    #NB -fimplicit-none was dropped from the gfortran flags: it is applied to
    #NB f2py's own generated wrapper (kmc_model-f2pywrappers2.f90) as well,
    #NB which relies on implicit typing for character-returning functions such
    #NB as get_system_name and therefore fails to compile with it.
    if options.no_optimize:
        extra_flags['gfortran'] = ('-ffree-line-length-none -ffree-form' #-ffixed-line-length-none is not used as it seems to be not needed as of Nov 20th, 2022
                                   ' -xf95-cpp-input -Wall'
                                   ' -time  -fmax-identifier-length=63 ')
        extra_flags['gnu95'] = extra_flags['gfortran']
        extra_flags['intel'] = '-fpp -Wall -I/opt/intel/fc/10.1.018/lib'
        extra_flags['intelem'] = '-fpp -Wall'

    else:
        extra_flags['gfortran'] = ('-ffree-line-length-none -ffree-form' #-ffixed-line-length-none is not used as it seems to be not needed as of Nov 20th, 2022
                                   ' -xf95-cpp-input -Wall -O3'
                                   ' -time -fmax-identifier-length=63 ')
        extra_flags['gnu95'] = extra_flags['gfortran']
        extra_flags['intel'] = '-fast -fpp -Wall -I/opt/intel/fc/10.1.018/lib'
        extra_flags['intelem'] = '-fast -fpp -Wall'

    # FIXME
    extra_libs = ''
    ccompiler = ''
    if os.name == 'nt':
        ccompiler = '--compiler=mingw64'#'--compiler=mingw32'
        if sys.version_info < (2, 7):
            extra_libs = ' -lmsvcr71 '
        else:
            extra_libs = ' -lmsvcr90 '

    module_name = 'kmc_model'

    if not isfile('kind_values_f2py.f90'):
        evaluate_kind_values('kind_values.f90', 'kind_values_f2py.f90')

    for src_file in src_files:
        if not isfile(src_file):
            raise IOError('File %s not found' % src_file)

    call = []
    call.append('-c')
    call.append('-c')
    if os.name == 'nt':
        call.append('%s' % ccompiler)
    extra_flags = extra_flags.get(options.fcompiler, '')

    if options.debug:
        extra_flags += ' -DDEBUG'

    #NB The meson backend (the only one f2py offers on Python >= 3.12) builds
    #NB out of tree and copies the sources into a temporary directory, so
    #NB base.f90's #include "assert.ppc" no longer resolves next to the source
    #NB and the include files have to be put on the include path explicitly.
    #NB They are copied into a temporary directory rather than pointing -I at
    #NB the source directory because f2py splits --f90flags on whitespace
    #NB (numpy/f2py/_backends/_meson.py), and the source path contains spaces
    #NB whenever the model name does.
    import tempfile
    include_dir = tempfile.mkdtemp()
    for include_file in glob('*.ppc'):
        shutil.copy(include_file, include_dir)
    extra_flags += ' -I%s' % include_dir

    #NB --fcompiler is a distutils-backend option and is not understood by the
    #NB meson backend. The compiler is selected through the FC environment
    #NB variable instead, which meson honours.
    os.environ.setdefault('FC', fcompiler_executable(options.fcompiler))

    #NB presence of " around f90flags argument confuses f2py.
    #NB Command line argument separation already set by
    #NB split into separate str items in list. Not
    #NB sure why it ever worked.
    #NB call.append('--f90flags="%s"' % extra_flags)
    call.append('--f90flags=%s' % extra_flags)
    call.append('-m')
    call.append(module_name)
    call += src_files

    print(call)
    from copy import deepcopy
    true_argv = deepcopy(sys.argv)  # save for later
    from numpy import f2py
    sys.argv = call
    try:
        try:
            f2py.main()  # Doesn't work according to Alberdi, but works in Erwin's.
        except:
            from subprocess import call
            #'python3' is assumed to be the default command, but it could be 'python'. So we use "sys.executable" to avoid getting the wrong one.
            command = [sys.executable, '-m', 'numpy.f2py', '--f90flags=' + extra_flags, '-m',
                       module_name, '-c'] + src_files
            print(' '.join(command))
            call(command)
    finally:
        shutil.rmtree(include_dir, ignore_errors=True)
        sys.argv = true_argv


def T_grid(T_min, T_max, n):
    from numpy import linspace, array
    """Return a list of n temperatures between
       T_min and T_max such that the grid of T^(-1)
       is evenly spaced.
    """

    T_min1 = T_min ** (-1.)
    T_max1 = T_max ** (-1.)

    grid = list(linspace(T_max1, T_min1, n))
    grid.reverse()
    grid = [x ** (-1.) for x in grid]

    return array(grid)


def p_grid(p_min, p_max, n):
    from numpy import logspace, log10
    """Return a list of n pressures between
       p_min and p_max such that the grid of log(p)
       is evenly spaced.
    """
    p_minlog = log10(p_min)
    p_maxlog = log10(p_max)

    grid = logspace(p_minlog, p_maxlog, n)

    return grid


def timeit(func):
    """
    Generic timing decorator

    To stop time for function call f
    just ::
        from kmcos.utils import timeit
        @timeit
        def f():
            ...

     """
    def wrapper(*args, **kwargs):
        time0 = time()
        func(*args, **kwargs)
        print('Executing %s took %.3f s' % (func.__name__, time() - time0))
    return wrapper


def col_tuple2str(tup):
    """Convenience function that turns a HTML type color
    into a tuple of three float between 0 and 1
    """
    r, g, b = tup
    b *= 255
    res = '#'
    res += hex(int(255 * r))[-2:].replace('x', '0')
    res += hex(int(255 * g))[-2:].replace('x', '0')
    res += hex(int(255 * b))[-2:].replace('x', '0')

    return res


def col_str2tuple(hex_string):
    """Convenience function that turns a HTML type color
    into a tuple of three float between 0 and 1
    """
    import gtk
    try:
        color = gtk.gdk.Color(hex_string)
    except ValueError as e:
        raise UserWarning('GTK cannot decipher color string {hex_string}: {e}'.format(**locals()))
    return (color.red_float, color.green_float, color.blue_float)


def jmolcolor_in_hex(i):
    """Return a given jmol color in hexadecimal representation."""
    from ase.data.colors import jmol_colors
    color = [int(x) for x in 255 * jmol_colors[i]]
    r, g, b = color
    a = 255
    color = (r << 24) | (g << 16) | (b << 8) | a
    return color


def evaluate_template(template, escape_python=False, **kwargs):
    """Very simple template evaluation function using only exec and str.format()

    There are two flavors of the template language, depending on whether
    the python parts or the template parts are escaped.

    A template can use the full python syntax. Every line starts with '#@ '
    is interpreted as a template line. Please use proper indentation before
    and note the space after '#@'.

    The template lines are converted to TEMPLATE_LINE.format(locals())
    and thefore every variable in the template line should be escape
    with {}.

    A valid template could be

    for i in range:
        #@ Hello World {i}

    """
    #NB kwargs (e.g. self, data, options) used to be injected via
    #NB locals().update(kwargs), which relied on CPython <= 3.12 returning the
    #NB frame's cached f_locals. PEP 667 (3.13) makes locals() an independent
    #NB snapshot, so the kwargs are merged into the exec namespace explicitly
    #NB below instead. Real locals take precedence, as they did before.

    result = ''
    NEWLINE = '\n'
    PREFIX = '#@'
    lines = [line + NEWLINE for line in template.split(NEWLINE)]

    if escape_python:
        # first just replace verbose lines by pass to check syntax
        python_lines = ''
        matched = False
        for line in lines:
            if re.match('^\s*%s ?' % PREFIX, line):
                python_lines += line.lstrip()[3:]
                matched = True
            else:
                python_lines += 'pass # %s' % line.lstrip()
        # if the tempate didn't contain any meta strings
        # just return the original
        if not matched:
            return template
        #NB python3 exec doesn't modify local variables.
        #NB create local dict and copy back "result" explicitly
        #NB if any other local variables are modified, that change
        #NB will be lost.
        ldict = {**kwargs, **locals()}
        exec(python_lines, globals(), ldict)
        result = ldict['result']

        # second turn literary lines into write statements
        python_lines = ''
        for line in lines:
            if re.match('^\s*%s ' % PREFIX, line):
                python_lines += line.lstrip()[3:]
            elif re.match('^\s*%s$' % PREFIX, line):
                python_lines += '%sresult += "\\n"\n' % (
                    ' ' * (len(line) - len(line.lstrip())))
            elif re.match('^$', line):
                # python_lines += 'result += """\n"""\n'
                pass
            else:
                python_lines += '%sresult += ("""%s""".format(**dict(locals())))\n' \
                    % (' ' * (len(line.expandtabs(4)) - len(line.lstrip())),  line.lstrip())

        #NB see note above
        ldict = {**kwargs, **locals()}
        exec(python_lines, globals(), ldict)
        result = ldict['result'] 

    else:
        # first just replace verbose lines by pass to check syntax
        python_lines = ''
        matched = False
        for line in lines:
            if re.match('\s*%s ?' % PREFIX, line):
                python_lines += '%spass %s' \
                    % (' ' * (len(line) - len(line.lstrip())),
                       line.lstrip())

                matched = True
            else:
                python_lines += line
        if not matched:
            return template
        #NB see note above
        ldict = {**kwargs, **locals()}
        exec(python_lines, globals(), ldict)
        result = ldict['result']

        # second turn literary lines into write statements
        python_lines = ''
                                             
        for line in lines:
            if re.match('\s*%s ' % PREFIX, line):
                python_lines += '%sresult += ("""%s""".format(**dict(locals())))\n' \
                    % (' ' * (len(line) - len(line.lstrip())),
                       line.lstrip()[3:])
            elif re.match('\s*%s' % PREFIX, line):
                python_lines += '%sresult += "\\n"\n' % (
                    ' ' * (len(line) - len(line.lstrip())))
            else:
                python_lines += line

        #NB see note above
        ldict = {**kwargs, **locals()}
        exec(python_lines, globals(), ldict) 
        result = ldict['result']

    return result
