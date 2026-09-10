# the reaction rates are way off (time of reaction is way too fast)
# fix it later, write presentation first

import math

import numpy as np

import kmcos
from kmcos.io import *
from kmcos.types import *

pt = kmcos.create_kmc_model()
pt.set_meta(
    author="Lucas Yuan",
    email="lucasmyuan@gmail.com",
    model_name="CO2 Reduction to CO (with salt precipitation)",
    model_dimension=2,
)

# the geometry is just to make it look good, it doesn't actually matter for the simulation.

d_CO_double = 1.20
d_CO_single = 1.33
d_OH = 0.97

d_CO_triple = 1.13

pos_C_COOH = [0, 0, 0]
pos_O_double_COOH = [-d_CO_double * math.sqrt(3) / 2, 0, d_CO_double / 2]
pos_O_single_COOH = [d_CO_single * math.sqrt(3) / 2, 0, d_CO_single / 2]
delta_H_COOH = [
    -d_OH * math.sin(math.radians(14)),
    0,
    d_OH * math.cos(math.radians(14)),
]
pos_H_COOH = [a + b for a, b in zip(pos_O_single_COOH, delta_H_COOH)]

pos_COOH = [pos_C_COOH, pos_O_double_COOH, pos_O_single_COOH, pos_H_COOH]

pos_CO = [[0, 0, 0], [0, 0, d_CO_triple]]

pt.add_species(name="empty")

pt.add_species(
    name="CO2", representation="Atoms('OCO', [[0, 0, 0], [0, 0, 0], [0, 0, 0]])"
)

pt.add_species(name="COOH", representation=f"Atoms('COOH',{pos_COOH})")

pt.add_species(name="CO", representation=f"Atoms('CO', {pos_CO})")

layer = pt.add_layer(name="simple_cubic")

layer.sites.append(Site(name="Ag_site", pos="0.5 0.5 0.5", default_species="empty"))

# NOTE: all delta G values are at a voltage of -0.11 V relative to RHE?
# find better sources for voltages.
# Current sources are here: "electrochemical co2-to-co conversion a comprehensive review"

K_BOLTZMANN = 8.61733326e-5  # eV/K
PREFACTOR = 1e13  # Hz
PLANCK = 4.1356677e-15  # eV s

cell_width = 2.8892
temp = 293.15
p_CO2 = 1.0
# p_CO = 1.
deltaG_CO2_COOH = 1.0
deltaG_COOH_CO = -0.632
deltaG_CO_COfree = -0.423
bias_v = -3.0

pt.lattice.cell = np.diag([cell_width, cell_width, 5])

pt.add_parameter(name="T", value=temp, adjustable=True, min=100, max=700)

# find defaults for partial pressure based off of saturation concentrations.

pt.add_parameter(name="p_CO2", value=p_CO2, adjustable=True, min=1e-10, max=1.0e2)
# pt.add_parameter(name='p_CO', value=p_CO, adjustable=True, min=1e-10, max=1.e2)
pt.add_parameter(name="A", value=f"({cell_width}*angstrom)**2")
pt.add_parameter(
    name="deltaG_CO2_COOH", value=deltaG_CO2_COOH, adjustable=True, min=-2, max=2
)
pt.add_parameter(
    name="deltaG_COOH_CO", value=deltaG_COOH_CO, adjustable=True, min=-2, max=2
)
pt.add_parameter(
    name="deltaG_CO_COfree", value=deltaG_CO_COfree, adjustable=True, min=-2, max=2
)
pt.add_parameter(name="bias_v", value=bias_v, adjustable=True, min=-6, max=0)

pt.add_parameter(name="CO2_COOH", value=1.0, adjustable=True, min=1e-8, max=1e8)
# pt.add_parameter(name='COOH_de', value=1, adjustable=True, min=1e-8, max=1e8)
pt.add_parameter(name="COOH_CO", value=1.0, adjustable=True, min=1e-8, max=1e8)
pt.add_parameter(name="CO_de", value=1.0, adjustable=True, min=1e-8, max=1e8)
pt.add_parameter(name="PREFACTOR", value=PREFACTOR, adjustable=True, min=1e-8, max=1e20)

# figure out how to get the rate constant. either the eyring equation or kinetic theory.
# actually, it should be chemisorption (obviously creating a bond), so use eyring equation.

# okay, here's the full picture for how you get the adsorption rates.
# each adsorption rate is dprob/dt for a single site. so for ad,
# we use the p*A*hertz knudsen term*TST exp term.
# for COOH-CO, we just use the TST exp term.
# For de, search it up or use detailed balance.
# The bigger issue is the fact that the adsorption energies
# are really high. why does that happen?


def k_htst(t, diffG):
    exp_factor = -diffG / (t * K_BOLTZMANN)
    return PREFACTOR * math.exp(exp_factor)


coord = pt.lattice.generate_coord("Ag_site.(0, 0, 0).simple_cubic")

pt.add_process(
    name="CO2_COOH",
    conditions=[Condition(coord=coord, species="empty")],
    actions=[Action(coord=coord, species="COOH")],
    rate_constant="p_CO2*bar*A/sqrt(2*pi*umass*m_CO2/beta)*exp(-(deltaG_CO2_COOH+0.5*bias_v)*eV*beta)*CO2_COOH",
)  # -bias_v term due to applied potential
# 0.5 term used bc of transfer coefficient

# pt.add_process(name='COOH_de',
#                conditions=[Condition(coord=coord, species='COOH')],
#                actions=[Action(coord=coord, species='empty')],
#                rate_constant=f'p_CO2*bar*A*CO2_COOH*{k_eyring(temp, deltaG_CO2_COOH)}')

pt.add_process(
    name="COOH_CO",
    conditions=[Condition(coord=coord, species="COOH")],
    actions=[Action(coord=coord, species="CO")],
    rate_constant="PREFACTOR*exp(-deltaG_COOH_CO*eV*beta)*COOH_CO",
)

pt.add_process(
    name="CO_de",
    conditions=[Condition(coord=coord, species="CO")],
    actions=[Action(coord=coord, species="empty")],
    rate_constant="PREFACTOR*exp(-deltaG_CO_COfree*eV*beta)*CO_de",
)

pt.filename = "co2rr.xml"
pt.save()
