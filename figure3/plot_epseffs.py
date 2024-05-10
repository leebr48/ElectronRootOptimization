#Inputs
epseffMax = 5
axisFontSize = 24
legendFontSize = 13
xSizeInches = 8
ySizeInches = 6
fileExt = 'pdf'
dpi = 600

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
configuration1_epseff = np.loadtxt('configuration1_epseff.txt')
configuration2_epseff = np.loadtxt('configuration2_epseff.txt')
configuration3_epseff = np.loadtxt('configuration3_epseff.txt')
w7xhm_epseff = np.loadtxt('w7xhm_epseff.txt')

configuration1_wout = netcdf_file('../configurations/configuration1/stage3/wout_configuration1_stage3.nc', mode='r', mmap=False)
configuration2_wout = netcdf_file('../configurations/configuration2/wout_configuration2.nc', mode='r', mmap=False)
configuration3_wout = netcdf_file('../configurations/configuration3/wout_configuration3.nc', mode='r', mmap=False)
w7xhm_wout = netcdf_file('../configurations/w7xhm/wout_w7xhm.nc', mode='r', mmap=False)
configuration1_ns = configuration1_wout.variables['ns'][()]
configuration2_ns = configuration2_wout.variables['ns'][()]
configuration3_ns = configuration3_wout.variables['ns'][()]
w7xhm_ns = w7xhm_wout.variables['ns'][()]
if configuration1_ns == configuration2_ns == configuration3_ns == w7xhm_ns:
    ns = configuration1_ns
else:
    raise IOError('"ns" for the initial and optimized configurations differ - something is wrong.')

# Process data
_, fulls = createVMECGrids(ns)
sgrid = fulls[1:] # Ignore the magnetic axis because eps_eff cannot be evaluated there by NEO.
rhogrid = np.sqrt(sgrid)
data = np.column_stack((rhogrid, configuration1_epseff, configuration2_epseff, configuration3_epseff, w7xhm_epseff))

# Plot data
plt.subplots(figsize=(xSizeInches, ySizeInches))
plt.plot(data[:,0], data[:,1])
plt.plot(data[:,0], data[:,2])
plt.plot(data[:,0], data[:,3])
plt.plot(data[:,0], data[:,4])
plt.yticks(np.arange(0,np.ceil(np.max(data[:,1]))+1, 1))
plt.xlim(xmin=0, xmax=1)
plt.ylim(ymax=epseffMax)
plt.gca().xaxis.set_major_formatter(formatter)
plt.xlabel(r'$\rho$')
plt.ylabel(r'$\epsilon_\mathrm{eff}$ (%)')
plt.legend(['Configuration 1', 'Configuration 2', 'Configuration 3', 'W7-X High-Mirror'])
plt.savefig('epseffs'+'.'+fileExt, bbox_inches='tight', dpi=dpi)

plt.show()
