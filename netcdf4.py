# Using netCDF4 datasets in Python

import netCDF4
import numpy as np # Intro to numpy: https://www.youtube.com/watch?v=QUT1VHiLmmI

# This is boilerplate code to open a netCDF file and use the contents with numpy
# https://github.com/Unidata/netcdf4-python/blob/master/examples/reading_netCDF.ipynb

f = netCDF4.Dataset('c3s_obs-sl_glo_phy-ssh_my_twosat-l4-duacs-0.25deg_P1D_1710527666697.nc')
# print(f) 

print(f.variables.keys()) # get all variable names
latitude = f.variables['latitude']; # print(latitude) 
longitude = f.variables['longitude']; # print(longitude)
time = f.variables['time']; # print(time)

for d in f.dimensions.items():
    print(d)
    
# latitude.dimensions
# latitude.shape

