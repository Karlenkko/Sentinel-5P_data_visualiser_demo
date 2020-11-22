# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm
from netCDF4 import Dataset
import cartopy.crs as ccrs
import matplotlib.cm as cm

if __name__ == '__main__':
    # print_hi('PyCharm')
    nc_file = 'S5P_OFFL_L2__NO2____20201102T221615_20201102T235745_15841_01_010302_20201104T150825.nc'
    fh = Dataset(nc_file, mode = 'r')
    # print(fh.groups['PRODUCT'].variables['nitrogendioxide_tropospheric_column_precision'])
    lons = fh.groups['PRODUCT'].variables['longitude'][:][0, :, :]
    lats = fh.groups['PRODUCT'].variables['latitude'][:][0, :, :]
    no2 = fh.groups['PRODUCT'].variables['nitrogendioxide_tropospheric_column_precision'][0, :, :]
    no2_units = fh.groups['PRODUCT'].variables['nitrogendioxide_tropospheric_column_precision'].units

    lon_0 = lons.mean()
    lat_0 = lats.mean()
    print(no2.shape)


