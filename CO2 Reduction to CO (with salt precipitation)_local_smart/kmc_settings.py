model_name = 'CO2 Reduction to CO (with salt precipitation)'
simulation_size = 20 #TODO: A. Savara found on 12/04/22 that this is hardcoded in io.py, and it should not be hardcoded. 
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
    "A":{"value":"(2.8892*angstrom)**2", "adjustable":False, "min":"0.0", "max":"0.0","scale":"linear"},
    "CO2_COOH":{"value":"1.0", "adjustable":True, "min":"1e-08", "max":"100000000.0","scale":"linear"},
    "COOH_CO":{"value":"1.0", "adjustable":True, "min":"1e-08", "max":"100000000.0","scale":"linear"},
    "CO_de":{"value":"1.0", "adjustable":True, "min":"1e-08", "max":"100000000.0","scale":"linear"},
    "PREFACTOR":{"value":"10000000000000.0", "adjustable":True, "min":"1e-08", "max":"1e+20","scale":"linear"},
    "T":{"value":"293.15", "adjustable":True, "min":"100.0", "max":"700.0","scale":"linear"},
    "bias_v":{"value":"-3.0", "adjustable":True, "min":"-6.0", "max":"0.0","scale":"linear"},
    "deltaG_CO2_COOH":{"value":"1.0", "adjustable":True, "min":"-2.0", "max":"2.0","scale":"linear"},
    "deltaG_COOH_CO":{"value":"-0.632", "adjustable":True, "min":"-2.0", "max":"2.0","scale":"linear"},
    "deltaG_CO_COfree":{"value":"-0.423", "adjustable":True, "min":"-2.0", "max":"2.0","scale":"linear"},
    "p_CO2":{"value":"1.0", "adjustable":True, "min":"1e-10", "max":"100.0","scale":"linear"},
    }

rate_constants = {
    "CO2_COOH":("p_CO2*bar*A/sqrt(2*pi*umass*m_CO2/beta)*exp(-(deltaG_CO2_COOH+0.5*bias_v)*eV*beta)*CO2_COOH", True),
    "COOH_CO":("PREFACTOR*exp(-deltaG_COOH_CO*eV*beta)*COOH_CO", True),
    "CO_de":("PREFACTOR*exp(-deltaG_CO_COfree*eV*beta)*CO_de", True),
    }

site_names = ['simple_cubic_Ag_site']
representations = {
    "CO":"""Atoms('CO', [[0, 0, 0], [0, 0, 1.13]])""",
    "CO2":"""Atoms('OCO', [[0, 0, 0], [0, 0, 0], [0, 0, 0]])""",
    "COOH":"""Atoms('COOH',[[0, 0, 0], [-1.0392304845413263, 0, 0.6], [1.1518137870333034, 0, 0.665], [0.9171495483016257, 0, 1.6061868544877167]])""",
    "empty":"""""",
    }

lattice_representation = """"""

species_tags = {
    "CO":"""""",
    "CO2":"""""",
    "COOH":"""""",
    "empty":"""""",
    }

tof_count = {
    }

connected_variables={'surroundingSitesDict': {}}
xml = """<?xml version="1.0" ?>
<kmc version="(0, 4)">
    <meta author="Lucas Yuan" email="lucasmyuan@gmail.com" model_name="CO2 Reduction to CO (with salt precipitation)" model_dimension="2" debug="0"/>
    <species_list default_species="empty">
        <species name="CO" representation="Atoms('CO', [[0, 0, 0], [0, 0, 1.13]])" color="" tags=""/>
        <species name="CO2" representation="Atoms('OCO', [[0, 0, 0], [0, 0, 0], [0, 0, 0]])" color="" tags=""/>
        <species name="COOH" representation="Atoms('COOH',[[0, 0, 0], [-1.0392304845413263, 0, 0.6], [1.1518137870333034, 0, 0.665], [0.9171495483016257, 0, 1.6061868544877167]])" color="" tags=""/>
        <species name="empty" representation="" color="" tags=""/>
    </species_list>
    <parameter_list>
        <parameter name="A" value="(2.8892*angstrom)**2" adjustable="False" min="0.0" max="0.0" scale="linear"/>
        <parameter name="CO2_COOH" value="1.0" adjustable="True" min="1e-08" max="100000000.0" scale="linear"/>
        <parameter name="COOH_CO" value="1.0" adjustable="True" min="1e-08" max="100000000.0" scale="linear"/>
        <parameter name="CO_de" value="1.0" adjustable="True" min="1e-08" max="100000000.0" scale="linear"/>
        <parameter name="PREFACTOR" value="10000000000000.0" adjustable="True" min="1e-08" max="1e+20" scale="linear"/>
        <parameter name="T" value="293.15" adjustable="True" min="100.0" max="700.0" scale="linear"/>
        <parameter name="bias_v" value="-3.0" adjustable="True" min="-6.0" max="0.0" scale="linear"/>
        <parameter name="deltaG_CO2_COOH" value="1.0" adjustable="True" min="-2.0" max="2.0" scale="linear"/>
        <parameter name="deltaG_COOH_CO" value="-0.632" adjustable="True" min="-2.0" max="2.0" scale="linear"/>
        <parameter name="deltaG_CO_COfree" value="-0.423" adjustable="True" min="-2.0" max="2.0" scale="linear"/>
        <parameter name="p_CO2" value="1.0" adjustable="True" min="1e-10" max="100.0" scale="linear"/>
    </parameter_list>
    <lattice cell_size="2.8892 0.0 0.0 0.0 2.8892 0.0 0.0 0.0 5.0" default_layer="simple_cubic" substrate_layer="simple_cubic" representation="">
        <layer name="simple_cubic" color="#ffffff">
            <site pos="0.5 0.5 0.5" type="Ag_site" tags="" default_species="empty"/>
        </layer>
    </lattice>
    <process_list>
        <process rate_constant="p_CO2*bar*A/sqrt(2*pi*umass*m_CO2/beta)*exp(-(deltaG_CO2_COOH+0.5*bias_v)*eV*beta)*CO2_COOH" name="CO2_COOH" enabled="True">
            <condition species="empty" coord_layer="simple_cubic" coord_name="Ag_site" coord_offset="0 0 0"/>
            <action species="COOH" coord_layer="simple_cubic" coord_name="Ag_site" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="PREFACTOR*exp(-deltaG_COOH_CO*eV*beta)*COOH_CO" name="COOH_CO" enabled="True">
            <condition species="COOH" coord_layer="simple_cubic" coord_name="Ag_site" coord_offset="0 0 0"/>
            <action species="CO" coord_layer="simple_cubic" coord_name="Ag_site" coord_offset="0 0 0"/>
        </process>
        <process rate_constant="PREFACTOR*exp(-deltaG_CO_COfree*eV*beta)*CO_de" name="CO_de" enabled="True">
            <condition species="CO" coord_layer="simple_cubic" coord_name="Ag_site" coord_offset="0 0 0"/>
            <action species="empty" coord_layer="simple_cubic" coord_name="Ag_site" coord_offset="0 0 0"/>
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
