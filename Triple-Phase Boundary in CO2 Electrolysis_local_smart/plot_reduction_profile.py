#!/usr/bin/env python3
"""Plot CO2 reduction events per catalyst site, and how that profile builds up.

Every catalyst site along the surface has its own reduction process
(reduction_1 ... reduction_N, site 1 sitting at the triple-phase boundary and
site N deepest into the electrolyte), so the per-process counters kmcos keeps
are already the profile we want: procstat[reduction_y] is the number of times
CO2 was reduced at site y.

Run this from the model directory, i.e. the one holding kmc_model*.so and
kmc_settings.py::

    python plot_reduction_profile.py                 # ~20M steps, about a minute
    python plot_reduction_profile.py --steps 2000000 # quick look
"""

import argparse
import os
import sys

import numpy as np


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--steps', type=int, default=20000000,
                        help='total kMC steps to run (default: %(default)s)')
    parser.add_argument('--snapshots', type=int, default=60,
                        help='how many times to read the counters along the way'
                             ' (default: %(default)s)')
    parser.add_argument('--equilibrate', type=int, default=0,
                        help='steps to run before the counters are read the first'
                             ' time; these events still count (default: %(default)s)')
    parser.add_argument('--out', default='reduction_profile.png',
                        help='where to write the figure (default: %(default)s)')
    parser.add_argument('--show', action='store_true',
                        help='also open the figure in a window')
    return parser.parse_args()


def find_reduction_processes(model):
    """(site number, process index) for every reduction_<site> process.

    Read off the model rather than hardcoded, so this keeps working when
    NUM_CATALYST_SITES changes in tpb.py.
    """
    processes = []
    site = 1
    while True:
        try:
            index = getattr(model.proclist, 'reduction_%i' % site)
        except AttributeError:
            break
        processes.append((site, int(index)))
        site += 1
    return processes


def run(model, processes, steps, snapshots, equilibrate):
    """Run the model, reading the counters `snapshots` times along the way.

    Returns the kMC times of the readings and the cumulative event counts,
    shape (snapshots + 1, nr of sites), with the state at the start as row 0.
    """
    indices = [index for _, index in processes]

    def counts():
        return np.array([model.base.get_procstat(index) for index in indices],
                        dtype=float)

    if equilibrate:
        model.do_steps(equilibrate)

    times = [model.base.get_kmc_time()]
    history = [counts()]

    chunk = max(1, steps // snapshots)
    for snapshot in range(snapshots):
        model.do_steps(chunk)
        times.append(model.base.get_kmc_time())
        history.append(counts())
        if (snapshot + 1) % 10 == 0 or snapshot + 1 == snapshots:
            print('  %2i/%i snapshots, %.3e s simulated, %i reduction events'
                  % (snapshot + 1, snapshots, times[-1], history[-1].sum()))

    return np.array(times), np.array(history)


def plot(sites, times, history, nr_of_copies, out, show):
    import matplotlib
    if not show:
        matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.colors import LogNorm

    # per-interval rate per individual site: the lattice holds nr_of_copies
    # periodic copies of every catalyst site, and they all count into the same
    # process counter
    intervals = np.diff(times)
    rates = np.diff(history, axis=0) / intervals[:, None] / nr_of_copies

    fig, (ax_profile, ax_heat) = plt.subplots(1, 2, figsize=(11.5, 4.6))

    # LEFT: the profile itself, redrawn at every snapshot and coloured by time
    colors = plt.get_cmap('viridis')
    norm = LogNorm(vmin=times[1], vmax=times[-1])
    for time, profile in zip(times[1:], history[1:]):
        ax_profile.plot(sites, profile, color=colors(norm(time)), lw=1, alpha=0.9)
    ax_profile.plot(sites, history[-1], 'o-', color='black', lw=1.6, ms=4,
                    label='final (%.2e s)' % times[-1])

    ax_profile.set_xlabel('catalyst site  (1 = triple-phase boundary)')
    ax_profile.set_ylabel('cumulative reduction events')
    ax_profile.set_title('Reduction events per catalyst site')
    ax_profile.set_xticks(sites)
    ax_profile.legend(loc='upper right', fontsize='small')
    ax_profile.grid(alpha=0.25)

    fig.colorbar(plt.cm.ScalarMappable(norm=norm, cmap=colors), ax=ax_profile,
                 label='kMC time (s)')

    # RIGHT: the same data as a rate, to show whether the shape is steady or
    # the active zone is still spreading into the electrolyte
    site_edges = np.arange(sites[0] - 0.5, sites[-1] + 1.5)
    positive = rates[rates > 0]
    # intervals in which a site saw no event at all are left grey rather than
    # painted as the darkest rate, so they read as "too few events here"
    heat_colors = plt.get_cmap('magma').copy()
    heat_colors.set_bad('0.9')
    mesh = ax_heat.pcolormesh(
        site_edges, times, np.ma.masked_where(rates <= 0, rates),
        cmap=heat_colors,
        norm=LogNorm(vmin=positive.min(), vmax=positive.max()) if positive.size else None,
        shading='flat')
    ax_heat.set_yscale('log')
    ax_heat.set_xlabel('catalyst site  (1 = triple-phase boundary)')
    ax_heat.set_ylabel('kMC time (s)')
    ax_heat.set_title('Reduction rate per site')
    ax_heat.set_xticks(sites)
    fig.colorbar(mesh, ax=ax_heat, label='reductions per site per second')

    fig.tight_layout()
    fig.savefig(out, dpi=150)
    print('\nwrote %s' % os.path.abspath(out))
    if show:
        plt.show()

    return rates


def report(sites, times, history, rates, nr_of_copies):
    total_time = times[-1] - times[0]
    print('\n%-6s %12s %14s %16s' % ('site', 'events', 'per site', 'per site per s'))
    for i, site in enumerate(sites):
        events = history[-1, i] - history[0, i]
        print('%-6i %12i %14.2f %16.3e'
              % (site, events, events / nr_of_copies,
                 events / nr_of_copies / total_time if total_time else float('nan')))
    print('%-6s %12i' % ('total', (history[-1] - history[0]).sum()))


def main():
    args = parse_args()

    from kmcos.run import KMC_Model

    model = KMC_Model(print_rates=False, banner=False)
    try:
        processes = find_reduction_processes(model)
        if not processes:
            sys.exit('No reduction_<site> processes in this model -- is this the '
                     'right directory?')
        sites = np.array([site for site, _ in processes])
        # every catalyst site is repeated once per unit cell of the lattice
        nr_of_copies = int(np.prod(model.lattice.system_size))

        print('%i catalyst sites, %i periodic copies of each, %i steps in %i snapshots'
              % (len(sites), nr_of_copies, args.steps, args.snapshots))
        times, history = run(model, processes, args.steps, args.snapshots,
                             args.equilibrate)
    finally:
        model.deallocate()

    rates = plot(sites, times, history, nr_of_copies, args.out, args.show)
    report(sites, times, history, rates, nr_of_copies)


if __name__ == '__main__':
    main()
