# Using the Copernicus Marine API
# https://help.marine.copernicus.eu/en/articles/8286883-copernicus-marine-toolbox-api-get-original-files

# pip install copernicusmarine
import copernicusmarine
from pprint import pprint

# These are the datasets from https://data.marine.copernicus.eu/product/SEALEVEL_GLO_PHY_CLIMATE_L4_MY_008_057/services
# ~108gb each
dataset_id_1 = "c3s_obs-sl_glo_phy-ssh_my_twosat-l4-duacs-0.25deg_P1D"
dataset_id_2 = "c3s_obs-sl_glo_phy-ssh_myint_twosat-l4-duacs-0.25deg_P1D"

# Saves data to a folder
get_data_1 = copernicusmarine.get(
    dataset_id = dataset_id_1,
    filter = "",
    no_directories = True,
    output_directory = "data/1" 
)

get_data_2 = copernicusmarine.get(
    dataset_id = dataset_id_2,
    filter = "",
    no_directories = True,
    output_directory = "data/2" 
)

pprint(f"List of saved files: {get_data_1}")