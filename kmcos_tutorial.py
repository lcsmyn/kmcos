import numpy as np

import kmcos
from kmcos.io import *
from kmcos.types import *

pt = kmcos.create_kmc_model()
pt.set_meta(
    author="Your Name",
    email="your.name@server.com",
    model_name="MyFirstModel",
    model_dimension=2,
)

pt.add_species(name="empty")

pt.add_species(name="CO", representation="Atoms('CO',[[0,0,0],[0,0,1.2]])")

layer = pt.add_layer(name="simple_cubic")

layer.sites.append(Site(name="hollow", pos="0.5 0.5 0.5", default_species="empty"))

pt.lattice.cell = np.diag([3.5, 3.5, 10])

pt.add_parameter(name="T", value=600.0, adjustable=True, min=400, max=800)
pt.add_parameter(name="p_CO", value=1.0, adjustable=True, min=1e-10, max=1.0e2)

pt.add_parameter(name="A", value="(3.5*angstrom)**2")

pt.add_parameter(name="deltaG", value="-0.5", adjustable=True, min=-1.3, max=0.3)

coord = pt.lattice.generate_coord("hollow.(0,0,0).simple_cubic")

pt.add_process(
    name="CO_adsorption",
    conditions=[Condition(coord=coord, species="empty")],
    actions=[Action(coord=coord, species="CO")],
    rate_constant="p_CO*bar*A/sqrt(2*pi*umass*m_CO/beta)",
)

pt.add_process(
    name="CO_desorption",
    conditions=[Condition(coord=coord, species="CO")],
    actions=[Action(coord=coord, species="empty")],
    rate_constant="p_CO*bar*A/sqrt(2*pi*umass*m_CO/beta)*exp(beta*deltaG*eV)*100000",
)

pt.print_statistics()
pt.backend = 'local_smart' #specifying is optional. 'local_smart' is the default. Currently, the other options are 'lat_int' and 'otf'
pt.clear_model() #This line is optional: if you are updating a model, this line will remove the old model files (including compiled files) before exporting the new one. It is convenient to always include this line because then you don't need to 'confirm' removing/overwriting the old model during the compile step.
pt.save_model()
kmcos.compile(pt)
