from itertools import combinations
import math

import numpy as np
import matplotlib.pyplot as plt

import kmcos
from kmcos.io import *
from kmcos.types import *

pt = kmcos.create_kmc_model()
pt.set_meta(
    author="Lucas Yuan",
    email="lucasmyuan@gmail.com",
    model_name="Triple-Phase Boundary in CO2 Electrolysis",
    model_dimension=1,
)

d_CO_double = 1.20
d_CO_single = 1.33
d_CO_in_CO3 = 1.28
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

pos_OH = [[0.0, 0.0, 0.0], [0.0, 0.0, d_OH]]

pos_CO3 = [
    [0.0, 0.0, 0.0],
    [0.0, 0.0, d_CO_in_CO3],
    [d_CO_in_CO3 * math.sqrt(3) / 2, 0.0, -d_CO_in_CO3 / 2],
    [-d_CO_in_CO3 * math.sqrt(3) / 2, 0.0, -d_CO_in_CO3 / 2],
]

NUM_CATALYST_SITES = 10
NUM_ELECTROLYTE_SITES = 10

PREFACTOR = 1e13

pt.add_species(name='empty')
pt.add_species(
    name="CO2", representation="Atoms('OCO', [[-1.163, 0, 0], [0, 0, 0], [1.163, 0, 0]])"
)
pt.add_species(name="COOH", representation=f"Atoms('COOH',{pos_COOH})")
pt.add_species(name="CO", representation=f"Atoms('CO', {pos_CO})")
pt.add_species(name="CO3", representation=f"Atoms('COOO',{pos_CO3})")
pt.add_species(name="OH", representation=f"Atoms('OH',{pos_OH})")
pt.add_species(name="Ag", representation="Atoms('Ag', [[0, 0, 0]])")

# cat_layer = pt.add_layer(name="cat_layer")
layer = pt.add_layer(name="tpb_line")

def get_name(y, z):
    str_coord = f'{y}_{z}'

    if z == 0:
        modifier = 'substrate'
    elif y == 0:
        modifier = 'boundary'
    elif z == 1:
        modifier = 'active'
    else:
        modifier = 'bulk'

    return str_coord + '_' + modifier

def get_modifier(site_name):
    return site_name.split("_")[2]

for y in range(NUM_CATALYST_SITES):
    for z in range(NUM_ELECTROLYTE_SITES+1):
        if z == 0:
            species = 'Ag'
        else:
            species = 'empty'

        layer.sites.append(Site(
            name=get_name(y, z),
            pos=f"0.5 {y/NUM_CATALYST_SITES} {z/(NUM_ELECTROLYTE_SITES+1)}", # leaving margin at the edge of cell
            default_species=species))

        # coord_dict.update({str_coord : pt.lattice.generate_coord(f'{site_name}.(0,0,0).tpb_line')})

site_width = 2.8892

pt.lattice.cell = np.diag([site_width,
                           site_width*(NUM_CATALYST_SITES-1),
                           site_width*(NUM_ELECTROLYTE_SITES)]) # we enforce height = width (for each sub-cell)
                                                                # so that diffusion term is correct

temp = 298.15
p_CO2 = 1.0
p_CO = 0.01

pt.add_parameter(name="T", value=temp, adjustable=True, min=100, max=700)
pt.add_parameter(name="p_CO2", value=p_CO2, adjustable=True, min=1e-10, max=1.0e2)
pt.add_parameter(name="A", value=f"({site_width}*angstrom)**2")
pt.add_parameter(name="CO2_dissolve", value=1, adjustable=True, min=1e-10, max=1e10)
pt.add_parameter(name="Ga_CO2_water_adsorb", value=0.094, adjustable=True, min=-1, max=1) # assume basic
pt.add_parameter(name="Ga_CO2_water_desorb", value=0.021, adjustable=True, min=-1, max=1) # assume basic
pt.add_parameter(name="Ga_CO2_dissolve", value=0.049, adjustable=True, min=-1, max=1) # assume basic
pt.add_parameter(name="Ga_CO2_undissolve", value=0.047, adjustable=True, min=-1, max=1) # assume basic
pt.add_parameter(name="CO2_diffuse", value=1, adjustable=True, min=1e-10, max=1e10)

pt.add_parameter(name="Ea_CO2_reduce", value=0.65, adjustable=True, min=-5, max=5)
pt.add_parameter(name="reduce", value=1, adjustable=True, min=1e-10, max=1e10)

pt.add_parameter(name="p_CO", value=p_CO, adjustable=True, min=1e-10, max=1.0e2) # We make p_CO very small so that most of the CO mass transport is due
                                                                                # to the CO2RR on the catalyst.
pt.add_parameter(name="deltaG_CO_dissolve", value=0.1, adjustable=True, min=-1, max=1) # estimate from "The hydration structure of carbon monoxide"
pt.add_parameter(name="CO_dissolve", value=1, adjustable=True, min=1e-10, max=1e10)
pt.add_parameter(name="CO_diffuse", value=1, adjustable=True, min=1e-10, max=1e10)

pt.add_parameter(name="OH_diffuse", value=1, adjustable=True, min=1e-10, max=1e10)
pt.add_parameter(name="CO3_diffuse", value=1, adjustable=True, min=1e-10, max=1e10)


DIFFUSION_CO2 = 1.92e-9 # m^2 / s at 298 K in water, according to Wikipedia
DIFFUSION_OH = 5.3e-9 # m^2 / s at 298 K in water, according to https://www.aqion.de/site/diffusion-coefficients
DIFFUSION_CO = 2.3e-9 # m^2 / s at 298 K in water, according to temperature dependence of diffusion coefficient of CO in water
DIFFUSION_CO3 = 0.955e-9 # m^2 / s  at 298 K in water, according to https://www.aqion.de/site/diffusion-coefficients

# Every mobile solute hops with the same nearest-neighbour scheme; only the
# diffusion coefficient and the adjustable scaling parameter differ.
DIFFUSING_SPECIES = [
    ("CO2", DIFFUSION_CO2, "CO2_diffuse"),
    # ("CO", DIFFUSION_CO, "CO_diffuse"),
    ("OH", DIFFUSION_OH, "OH_diffuse"),
    ("CO3", DIFFUSION_CO3, "CO3_diffuse"),
]

# SINGLE-SITE CHANNELS
# Temporal acceleration pairs two processes when one's conditions are the
# other's actions and vice versa. It matches on that signature alone, so two
# processes that describe the same transition -- same conditions, same actions,
# different rate constant -- are indistinguishable to it and each of them pairs
# with both members of the opposite pair. kmcos then counts more pairs than it
# has processes and raises 'not all processes could be paired', even though
# every process here does have a reverse.
#
# Every process that just swaps one species for `empty` on a single site has
# that shape, and three of them collide: the corner site (y = last, z = last) is
# an open boundary in both y and z, and the top of the y = 0 column is both a
# gas-exchange site and an open boundary in z.
#
# Independent kMC channels for the same transition are Poisson processes, so the
# physics is unchanged if we emit one process per (species, site) whose rate is
# the sum of the channel rates. That is what this accumulator does; the
# processes are written out once both loops below have contributed.

single_site_channels = {}

def add_single_site_channel(species, y, z, forward_rate, reverse_rate,
                            forward_name=None, reverse_name=None):
    """Register a `species@site <-> empty@site` channel.

    forward is species -> empty, reverse is empty -> species. Repeated calls for
    the same (species, y, z) add their rates to the existing channel rather than
    creating a second, identically shaped process. The first caller names it.
    """
    channel = single_site_channels.setdefault((species, y, z), {
        'forward_name': forward_name or f"escape_{species}_{y}_{z}",
        'reverse_name': reverse_name or f"escape_rev_{species}_{y}_{z}",
        'forward_rates': [],
        'reverse_rates': [],
    })
    channel['forward_rates'].append(forward_rate)
    channel['reverse_rates'].append(reverse_rate)

for z in range(1, NUM_ELECTROLYTE_SITES+1):
    # CO2 DISSOLUTION PROCESS

    # we assume Ea = Ga and use the values from Zhu 25. The difference Ea - Ga is ~k_B T, which is a factor
    # of e in the rate constant --> we can neglect for now.

    # CO2 adsorption is given b the hertz knudsen term times arrhenius term. CO2 desorption is more complicated.
    #

    add_single_site_channel(
        "CO2", 0, z,
        forward_rate="bar*A/sqrt(2*pi*umass*m_CO2/beta)*exp(-Ga_CO2_water_desorb*eV*beta)*CO2_dissolve",
        reverse_rate="p_CO2*bar*A/sqrt(2*pi*umass*m_CO2/beta)*exp(-Ga_CO2_water_adsorb*eV*beta)*CO2_dissolve",
        forward_name=f"water_adsorb_CO2_{z}",
        reverse_name=f"water_desorb_CO2_{z}",
    )

    # same for CO

    # add_single_site_channel(
    #     "CO", 0, z,
    #     forward_rate=f"{PREFACTOR}*CO_dissolve",
    #     reverse_rate="p_CO*bar*A/sqrt(2*pi*umass*m_CO/beta)*exp(-deltaG_CO_dissolve*eV*beta)*CO_dissolve",
    #     forward_name=f"undissolve_CO_{z}",
    #     reverse_name=f"dissolve_CO_{z}",
    # )

    # transition between surface and bulk states for CO2

    boundary_site = get_name(0, z)
    bulk_site = get_name(1, z)

    pt.parse_and_add_process(
        f"dissolve_CO2_from_0_{z}; \
          CO2@{boundary_site} + empty@{bulk_site} -> empty@{boundary_site} + CO2@{bulk_site}; \
          {PREFACTOR}*exp(-Ga_CO2_dissolve*eV*beta)"
    )
    pt.parse_and_add_process(
        f"undissolve_CO2_from_0_{z}; \
          empty@{boundary_site} + CO2@{bulk_site} -> CO2@{boundary_site} + empty@{bulk_site}; \
          {PREFACTOR}*exp(-Ga_CO2_undissolve*eV*beta)"
    )

    # DIFFUSION PROCESSES

    for y in range(1, NUM_CATALYST_SITES):
        center_site = get_name(y, z)

        for species, diffusion, diffuse_param in DIFFUSING_SPECIES:
            rate = f"{diffusion}/A*{diffuse_param}"

            # Z-AXIS DIFFUSION

            if z != NUM_ELECTROLYTE_SITES:
                top_site = get_name(y, z+1)
                pt.parse_and_add_process(
                    f"diffuse_{species}_{y}_{z}_{y}_{z+1}; \
                      {species}@{center_site} + empty@{top_site} -> empty@{center_site} + {species}@{top_site}; \
                      {rate}" # we used D = ka^2/6, but k is the total rate, and we divide by
                              # 6 to get the directional rate constant.
                )
                pt.parse_and_add_process(
                    f"diffuse_{species}_{y}_{z+1}_{y}_{z}; \
                      empty@{center_site} + {species}@{top_site} -> {species}@{center_site} + empty@{top_site}; \
                      {rate}"
                )

            # Y-AXIS DIFFUSION

            if y != NUM_CATALYST_SITES-1:
                forward_site = get_name(y+1, z)
                pt.parse_and_add_process(
                    f"diffuse_{species}_{y}_{z}_{y+1}_{z}; \
                      {species}@{center_site} + empty@{forward_site} -> empty@{center_site} + {species}@{forward_site}; \
                      {rate}"
                )
                pt.parse_and_add_process(
                    f"diffuse_{species}_{y+1}_{z}_{y}_{z}; \
                      empty@{center_site} + {species}@{forward_site} -> {species}@{center_site} + empty@{forward_site}; \
                      {rate}"
                )

            # OPEN (ABSORBING) BOUNDARY CONDITIONS
            # The far edges in y (deep into the electrolyte, away from the gas
            # interface at y=0) and in z (top of the electrolyte) open onto bulk
            # electrolyte that acts as an infinite sink. Without these processes a
            # solute reaching the edge can only hop back inwards, which reflects it
            # and artificially piles up concentration at the boundary.
            #
            # Each open direction is a hop, at the usual directional rate, into a
            # neighbour that is held empty (concentration 0): this is a Dirichlet
            # c=0 condition on those two faces. The corner site is open in both y
            # and z, so it contributes twice and can escape in either direction,
            # as it should -- the accumulator sums the two into one process
            # rather than emitting two identically shaped ones.
            #
            # The reverse gets an artificially high rate constant because we
            # need to pair. Issue: species actually do go back from the
            # boundary, we need to take this into account. just extending the
            # size of cell might work, though.

            # if y == NUM_CATALYST_SITES-1 or z == NUM_ELECTROLYTE_SITES:
            #     for _ in range((y == NUM_CATALYST_SITES-1) + (z == NUM_ELECTROLYTE_SITES)):
            #         add_single_site_channel(
            #             species, y, z,
            #             forward_rate=rate,
            #             reverse_rate="0.01",
            #             forward_name=f"absorb_{species}_{y}_{z}",
            #             reverse_name=f"absorb_rev_{species}_{y}_{z}",
            #         )

            # X-AXIS DIFFUSION
            # note: boundary conditions are periodic, so we don't have to add it in

            pt.parse_and_add_process(
                f"diffuse_x_{species}_from_{y}_{z}; \
                    {species}@{center_site} + empty@{center_site}.(1, 0, 0) -> empty@{center_site} + {species}@{center_site}.(1, 0, 0); \
                    {rate}"
            )
            pt.parse_and_add_process(
                f"diffuse_x_{species}_to_{y}_{z}; \
                    empty@{center_site} + {species}@{center_site}.(1, 0, 0) -> {species}@{center_site} + empty@{center_site}.(1, 0, 0); \
                    {rate}"
            )

# Emit one process pair per (species, site) for everything registered above.



for (species, y, z), channel in single_site_channels.items():
    center_site = get_name(y, z)

    pt.parse_and_add_process(
        f"{channel['forward_name']}; \
          {species}@{center_site} -> empty@{center_site}; \
          {' + '.join(channel['forward_rates'])}"
    )
    pt.parse_and_add_process(
        f"{channel['reverse_name']}; \
          empty@{center_site} -> {species}@{center_site}; \
          {' + '.join(channel['reverse_rates'])}"
    )

# REACTION PROCESSES

for y in range(1, NUM_CATALYST_SITES):

    active_site = get_name(y, 1)

    # these are arbitrary and probably don't matter. but revisit them.
    oh_site_1 = get_name(y, 2)
    oh_site_2 = get_name(y, 3)

    # CO2 ADSORPTION AND REACTION
    # Note: after CO2 is adsorbed, the rest of the reaction steps have low barriers,
    # which means they happen almost instanteously. Thus we just let CO2 --> CO without
    # simulating the intermediate steps.

    # Also, CO is no longer in the picture because we don't know how it enters and exits
    # the electrolyte. So it is just gone from the simulation for now.

    pt.parse_and_add_process(
        f"reduction_{y}; \
          CO2@{active_site} -> OH@{oh_site_1} + OH@{oh_site_2}; \
          {PREFACTOR}*exp(-Ea_CO2_reduce*eV*beta)*reduce"
    )

    # the reverse process is needed for temporal acceleration, but it doesn't actually exist.
    # Thus the rate constant is set to an artifically high value.

    pt.parse_and_add_process(
        f"reduction_rev_{y}; \
          OH@{oh_site_1} + OH@{oh_site_2} -> CO2@{active_site}; \
          0.01"
    )

# pt.add_process(
#     name="test1",
#     conditions=[Condition(coord=coord, species="empty")],
#     actions=[Action(coord=coord, species="CO2")],
#     rate_constant="1e6",
# )

# pt.add_process(
#     name="test2",
#     conditions=[Condition(coord=coord, species="CO2")],
#     actions=[Action(coord=coord, species="empty")],
#     rate_constant="1e5",
# )

pt.print_statistics()
pt.backend = 'local_smart' #specifying is optional. 'local_smart' is the default. Currently, the other options are 'lat_int' and 'otf'
pt.save_model()

# for i in range(1, NUM_CATALYST_SITES+1):
#     layer.sites.append(Site(name=f"substrate{i}", pos=f"0.5 {(i-1)/NUM_CATALYST_SITES} 0", default_species="Ag"))

# for i in range(2, NUM_ELECTROLYTE_SITES+2):
#     layer.sites.append(Site(name=f"elec_surface{i}", pos=f"0.5 0 {(i-1)/NUM_ELECTROLYTE_SITES}", default_species="empty"))

# for i in range(1, NUM_CATALYST_SITES+1):
#     layer.sites.append(Site(name=f"active_site{i}", pos=f"0.5 {(i-1)/NUM_CATALYST_SITES} {1/NUM_ELECTROLYTE_SITES}", default_species="empty"))

# for i in range(1, NUM_CATALYST_SITES+1):
#     for j in range(2, NUM_ELECTROLYTE_SITES+2):


# # note: in a more accurate model, the substrate should be an Ag(110) structure and
# # the active sites are between the terraces (actually, check this last part)

# layer.sites.append(Site(name="active_site", pos="0.5 0.5 0.1", default_species="empty"))

# for i in range(2, 11):
#     layer.sites.append(Site(name=f"bulk{i}", pos=f"0.5 0.5 {i/10}", default_species="empty"))

# processes to simulate:
# mass transport of co2 and co2 dissolving in electrolyte
# diffusion of co2 through electrolyte
# mass transport of K+ ions through electrolyte
# co2rr on catalyst surface
# competing HER on catalyst surface
# formation of salt on catalyst surface

# this means that we need to have the catalyst surface
# as a layer, and there needs to be an electrolyte-gas
# boundary area.

# the modeling of diffusion and transport of species
# is probably best done via mathematical models
# instead of kMC. Right? Yeah.

# first let's create a 2d plot of the concentration of
# co2 using the nernst planck equation (assuming no advection).
# we can plot this using matplotlib.

# huh, this actually looks like it will be pretty hard. there are
# researchers who write a paper implementing a library like this.

# use metropolis-hastings algorithm to get the equilibrium/steady state?

# for now, create a simple rectangular 2-d model with concentrations of
# co2, carbonate, K+, and OH-. Plot concentrations with numpy.

DIFFUSION_CO2 = 1.92e-9 # m^2 / s at 298 K in water, according to Wikipedia
DIFFUSION_K = 1.960e-9 # m^2 / s according to https://www.aqion.de/site/diffusion-coefficients
DIFFUSION_CO3 = 0.955e-9 # m^2 / s according to https://www.aqion.de/site/diffusion-coefficients
DIFFUSION_HCO3 = 1.180e-9 # same as above

# this paper is source for rate constants: https://epic.awi.de/id/eprint/13960/1/Sch2006g.pdf
