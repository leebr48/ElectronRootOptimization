#Inputs
presMin = 0
presMax = 1300
xSizeInches = 9
ySizeInches = 6

########################################################################################

# Import modules
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import os
import sys
from scipy.io import netcdf_file
sys.path.append(os.getenv('STELLOPTPLUSSFINCS_HOME')+'/src')
from dataProc import createVMECGrids
sys.path.append('../plotStandards')
from plotStandards import axisFontSize, legendFontSize, dpi, fileExt, colors

plt.rc('font', size=axisFontSize)
plt.rc('legend', fontsize=legendFontSize)

# Define handy function
def my_formatter(x, pos):
    if x == 0:
        return str(int(0))
    elif x == 1:
        return str(int(1))
    else:
        return '{0:.1f}'.format(x)

formatter = FuncFormatter(my_formatter)

# Load data
opt_wout = netcdf_file('../configurations/opt/wout_opt.nc', mode='r', mmap=False)

# Process data
all_s = opt_wout.variables['am_aux_s'][()]
all_pres = opt_wout.variables['am_aux_f'][()]

final_index = int(np.where(all_s == 1)[0] + 1)

s = all_s[:final_index]
pres = all_pres[:final_index] / 1000

# Plot data
plt.subplots(figsize=(xSizeInches, ySizeInches))
plt.plot(np.sqrt(s), pres, c=colors[0])
plt.yticks(np.arange(0,np.ceil(np.max(pres))+1, 200))
plt.xlim(xmin=0, xmax=1)
plt.ylim(ymin=presMin, ymax=presMax)
plt.gca().xaxis.set_major_formatter(formatter)
plt.xlabel(r'$\rho$')
plt.ylabel(r'Pressure (kPa)')
plt.savefig('pressure'+'.'+fileExt, bbox_inches='tight', dpi=dpi)
