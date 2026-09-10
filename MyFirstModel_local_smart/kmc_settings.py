model_name = 'MyFirstModel'
simulation_size = 20 #TODO: A. Savara found on 12/04/22 that this is hardcoded in io.py, and it should not be hardcoded. 
buffer_parameter = 1000 #TODO: A. Savara found on 12/04/22 that this block of settings is hardcoded in io.py, and it should not be hardcoded.
threshold_parameter = 0.2
sampling_steps = 20
execution_steps = 200
save_limit = 1000
random_seed = 1 #TODO: A. Savara found on 12/04/22 that this is hardcoded in io.py, and it should not be hardcoded.

def setup_model(model):
    """ Aug 15th 2022: setup_model is legacy code. Please ignore the rest of this comment and this function. 
    Write initialization steps here.
       e.g. ::
    model.put([0,0,0,model.lattice.default_a], model.proclist.species_a)
    """
    #from setup_model import setup_model
    #setup_model(model)
    pass

# Default history length in graph
hist_length = 30

parameters = {
    "A":{"value":"(3.5*angstrom)**2", "adjustable":False, "min":"0.0", "max":"0.0","scale":"linear"},
    "T":{"value":"600.0", "adjustable":True, "min":"400.0", "max":"800.0","scale":"linear"},
    "deltaG":{"value":"-0.5", "adjustable":True, "min":"-1.3", "max":"0.3","scale":"linear"},
    "p_CO":{"value":"1.0", "adjustable":True, "min":"1e-10", "max":"100.0","scale":"linear"},
    }

proc_pair_indices = [1, -1]

is_diff_proc = [False, False]

rate_constants = {
    "CO_adsorption":("p_CO*bar*A/sqrt(2*pi*umass*m_CO/beta)", True),
    "CO_desorption":("p_CO*bar*A/sqrt(2*pi*umass*m_CO/beta)*exp(beta*deltaG*eV)*100000", True),
    }

site_names = ['simple_cubic_hollow']
representations = {
    "CO":"""Atoms('CO',[[0,0,0],[0,0,1.2]])""",
    "empty":"""""",
    }

lattice_representation = """"""

species_tags = {
    "CO":"""""",
    "empty":"""""",
    }

tof_count = {
    }

connected_variables={'surroundingSitesDict': {}}
xml = """<?xml version="1.0" ?>
<kmc version="(0, 4)">
    <meta author="Your Name" email="your.name@server.com" model_name="MyFirstModel" model_dimension="2" debug="0"/>
    <species_list default_species="empty">
        <species name="CO" representation="Atoms('CO',[[0,0,0],[0,0,1.2]])" color="" tags=""/>
        <species name="empty" representation="" color="" tags=""/>
    </species_list>
    <parameter_list>
        <parameter name="A" value="(3.5*angstrom)**2" adjustable="False" min="0.0" max="0.0" scale="linear"/>
        <parameter name="T" value="600.0" adjustable="True" min="400.0" max="800.0" scale="linear"/>
        <parameter name="deltaG" value="-0.5" adjustable="True" min="-1.3" max="0.3" scale="linear"/>
        <parameter name="p_CO" value="1.0" adjustable="True" min="1e-10" max="100.0" scale="linear"/>
    </parameter_list>
    <lattice cell_size="3.5 0.0 0.0 0.0 3.5 0.0 0.0 0.0 10.0" default_layer="simple_cubic" substrate_layer="simple_cubic" representation="">
        <layer name="simple_cubic" color="#ffffff">
            <site pos="0.5 0.5 0.5" type="hollow" tags="" default_species="empty"/>
        </layer>
    </lattice>
    <process_list>
        <process rate_constant="p_CO*bar*A/sqrt(2*pi*umass*m_CO/beta)" name="CO_adsorption" enabled="True">
            <condition species="empty" coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0"/>
            <action species="CO" coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="p_CO*bar*A/sqrt(2*pi*umass*m_CO/beta)*exp(beta*deltaG*eV)*100000" name="CO_desorption" enabled="True">
            <condition species="CO" coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0"/>
        </process>
    </process_list>
    <output_list/>
    <connected_variables connected_variables_string="{'surroundingSitesDict': {}}"/>
</kmc>
"""
if __name__ == "__main__":
    #benchmark if kmc_settings.py is run without additional arguments, else call cli with additional argument provided.
    import sys
    if len(sys.argv) == 1:
        from kmcos import cli
        cli.main("benchmark")
    if len(sys.argv) == 2:
        from kmcos import cli
        cli.main(sys.argv[1])
