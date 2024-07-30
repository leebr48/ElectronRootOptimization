# This script was originally written by Hakan Smith.

# Inputs
lowerXLim = 1.0e-4
upperXLim = 1.0e0
lowerYLim = 1.5e-3
upperYLim = 5.0e1
xSizeInches = 8
ySizeInches = 8

# Code
import sys, os
import numpy as np
lib_path=os.getenv('NEOTRANSP_PYTHON_LIB')
sys.path.insert(0,lib_path)
from neolib import DKESdata, profile_data, transp_data, wait_for_user
import matplotlib.pyplot as plt
sys.path.append('../plotStandards')
from plotStandards import axisFontSize, legendFontSize, dpi, fileExt

plt.rc('font', size=axisFontSize)
plt.rc('legend', fontsize=legendFontSize)

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#% LOAD DATA FILES
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

dkfilew7xhm='w7xhm.dk'
bcfilew7xhm='w7xhm.bc'
dkfileOpt='opt.dk'
bcfileOpt='opt.bc'

dkw7xhm=DKESdata(dkfilew7xhm,bcfilew7xhm,reduced=False,minorradiusdefinition='W7AS')
dkOpt=DKESdata(dkfileOpt,bcfileOpt,reduced=False,minorradiusdefinition='W7AS')

rind=2 #Chosen radius index
rw7xhm=dkw7xhm.r[rind]
rOpt=dkOpt.r[rind]

figw7xhm, axw7xhm =dkw7xhm.plotD11star_vs_nustar(rw7xhm, errorbars=True, title='')
axw7xhm.set_xlim(left=lowerXLim, right=upperXLim)
axw7xhm.set_ylim(bottom=lowerYLim, top=upperYLim)
figw7xhm.set_size_inches(xSizeInches, ySizeInches)
figw7xhm.savefig('w7xhm_D11_vs_nu.' + fileExt, bbox_inches='tight', dpi=dpi)

figOpt, axOpt =dkOpt.plotD11star_vs_nustar(rOpt, errorbars=True, title='')
axOpt.set_xlim(left=lowerXLim, right=upperXLim)
axOpt.set_ylim(bottom=lowerYLim, top=upperYLim)
figOpt.set_size_inches(xSizeInches, ySizeInches)
figOpt.savefig('opt_D11_vs_nu.' + fileExt, bbox_inches='tight', dpi=dpi)
