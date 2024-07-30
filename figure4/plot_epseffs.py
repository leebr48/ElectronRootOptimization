#Inputs
epseffMin = 0
epseffMax = 3
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
opt_epseff = np.loadtxt('opt_epseff.txt')
w7xhm_epseff = np.loadtxt('w7xhm_epseff.txt')

opt_wout = netcdf_file('../configurations/opt/wout_opt.nc', mode='r', mmap=False)
w7xhm_wout = netcdf_file('../configurations/w7xhm/wout_w7xhm.nc', mode='r', mmap=False)
opt_ns = opt_wout.variables['ns'][()]
w7xhm_ns = w7xhm_wout.variables['ns'][()]
if opt_ns == w7xhm_ns:
    ns = opt_ns
else:
    raise IOError('"ns" for the initial and optimized configurations differ - something is wrong.')

# Process data
_, fulls = createVMECGrids(ns)
sgrid = fulls[1:] # Ignore the magnetic axis because eps_eff cannot be evaluated there by NEO.
rhogrid = np.sqrt(sgrid)
data = np.column_stack((rhogrid, opt_epseff, w7xhm_epseff))

# Plot data
plt.subplots(figsize=(xSizeInches, ySizeInches))
plt.plot(data[:,0], data[:,1], c=colors[0])
plt.plot(data[:,0], data[:,2], c=colors[1])
plt.yticks(np.arange(0,np.ceil(np.max(data[:,1]))+1, 1))
plt.xlim(xmin=0, xmax=1)
plt.ylim(ymin=epseffMin, ymax=epseffMax)
plt.gca().xaxis.set_major_formatter(formatter)
plt.xlabel(r'$\rho$')
plt.ylabel(r'$\epsilon_\mathrm{eff}$ (%)')
plt.legend(['Example Configuration', 'W7-X High-Mirror'])
plt.savefig('epseffs'+'.'+fileExt, bbox_inches='tight', dpi=dpi)
