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
dkfileConfig1='configuration1.dk'
bcfileConfig1='configuration1.bc'
dkfileConfig2='configuration2.dk'
bcfileConfig2='configuration2.bc'
dkfileConfig3='configuration3.dk'
bcfileConfig3='configuration3.bc'

dkw7xhm=DKESdata(dkfilew7xhm,bcfilew7xhm,reduced=False,minorradiusdefinition='W7AS')
dkConfig1=DKESdata(dkfileConfig1,bcfileConfig1,reduced=False,minorradiusdefinition='W7AS')
dkConfig2=DKESdata(dkfileConfig2,bcfileConfig2,reduced=False,minorradiusdefinition='W7AS')
dkConfig3=DKESdata(dkfileConfig3,bcfileConfig3,reduced=False,minorradiusdefinition='W7AS')

rind=2 #Chosen radius index
rw7xhm=dkw7xhm.r[rind]
rConfig1=dkConfig1.r[rind]
rConfig2=dkConfig2.r[rind]
rConfig3=dkConfig3.r[rind]

figw7xhm, axw7xhm =dkw7xhm.plotD11star_vs_nustar(rw7xhm, errorbars=True, title='')
axw7xhm.set_xlim(left=lowerXLim, right=upperXLim)
axw7xhm.set_ylim(bottom=lowerYLim, top=upperYLim)
figw7xhm.set_size_inches(xSizeInches, ySizeInches)
figw7xhm.savefig('w7xhm_D11_vs_nu.' + fileExt, bbox_inches='tight', dpi=dpi)

figConfig1, axConfig1 =dkConfig1.plotD11star_vs_nustar(rConfig1, errorbars=True, title='')
axConfig1.set_xlim(left=lowerXLim, right=upperXLim)
axConfig1.set_ylim(bottom=lowerYLim, top=upperYLim)
figConfig1.set_size_inches(xSizeInches, ySizeInches)
figConfig1.savefig('configuration1_D11_vs_nu.' + fileExt, bbox_inches='tight', dpi=dpi)

figConfig2, axConfig2 =dkConfig2.plotD11star_vs_nustar(rConfig2, errorbars=True, title='')
axConfig2.set_xlim(left=lowerXLim, right=upperXLim)
axConfig2.set_ylim(bottom=lowerYLim, top=upperYLim)
figConfig2.set_size_inches(xSizeInches, ySizeInches)
figConfig2.savefig('configuration2_D11_vs_nu.' + fileExt, bbox_inches='tight', dpi=dpi)

figConfig3, axConfig3 =dkConfig3.plotD11star_vs_nustar(rConfig3, errorbars=True, title='')
axConfig3.set_xlim(left=lowerXLim, right=upperXLim)
axConfig3.set_ylim(bottom=lowerYLim, top=upperYLim)
figConfig3.set_size_inches(xSizeInches, ySizeInches)
figConfig3.savefig('configuration3_D11_vs_nu.' + fileExt, bbox_inches='tight', dpi=dpi)
