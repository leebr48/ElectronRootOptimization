# This script is based on code from Alan Goodman.

# Inputs
fnames = ['../configurations/w7xhm/wout_w7xhm.nc', '../configurations/configuration1/stage3/wout_configuration1_stage3.nc', '../configurations/configuration2/wout_configuration2.nc', '../configurations/configuration3/wout_configuration3.nc']
figNames = ['w7xhm_lpk', 'configuration1_lpk', 'configuration2_lpk', 'configuration3_lpk']
xmins = [17, 35, 17, 17]
xmaxes = [25, 43, 25, 25]
ymin = -5.25
ymax = 5.25
numticks = 5

# Code
from matplotlib.ticker import LinearLocator
import matplotlib.pyplot as plt
import numpy as np
from simsopt.mhd.vmec import Vmec
import math
import sys
sys.path.append('../plotStandards')
from plotStandards import axisFontSize, dpi, fileExt, colors

plt.rc('font', size=axisFontSize)

for fname, figName, xmin, xmax in zip(fnames, figNames, xmins, xmaxes):

    xSizeInches = xmax - xmin
    ySizeInches = ymax - ymin

    vmec = Vmec(fname)

    nfp = vmec.wout.nfp
    lasym = vmec.wout.lasym
    xn = vmec.wout.xn
    xm = vmec.wout.xm
    xn_nyq = vmec.wout.xn_nyq
    xm_nyq = vmec.wout.xm_nyq
    rmnc = vmec.wout.rmnc.T
    zmns = vmec.wout.zmns.T
    raxis_cc = vmec.wout.raxis_cc
    zaxis_cs = vmec.wout.zaxis_cs
    nmodes = len(xn)
    ns = vmec.wout.ns
    if lasym == 1:
        rmns = vmec.wout.rmns
        zmnc = vmec.wout.zmnc
        raxis_cs = vmec.wout.raxis_cs
        zaxis_cc = vmec.wout.zaxis_cc
    else:
        rmns = 0*rmnc
        zmnc = 0*rmnc
        raxis_cs = 0*raxis_cc
        zaxis_cc = 0*raxis_cc

    fig = plt.figure(figsize=(xSizeInches, ySizeInches))
    fig.patch.set_facecolor('white')

    ntheta = 200
    nzeta = 5
    theta = np.linspace(0,2*np.pi,num=ntheta)
    zeta = np.linspace(0,np.pi/nfp,num=nzeta,endpoint=True)
    iradius = ns-1

    R = np.zeros((ntheta,nzeta))
    Z = np.zeros((ntheta,nzeta))
    for itheta in range(ntheta):
        for izeta in range(nzeta):
            for imode in range(nmodes):
                angle = xm[imode]*theta[itheta] - xn[imode]*zeta[izeta]
                R[itheta,izeta] = R[itheta,izeta] + rmnc[iradius,imode]*math.cos(angle) + rmns[iradius,imode]*math.sin(angle)
                Z[itheta,izeta] = Z[itheta,izeta] + zmns[iradius,imode]*math.sin(angle) + zmnc[iradius,imode]*math.cos(angle)

    for ind in range(nzeta):
        plt.plot(R[:,ind], Z[:,ind], '-', c=colors[ind])
        plt.plot(R[:,ind], Z[:,ind], '-', c=colors[ind])
        plt.plot(R[:,ind], Z[:,ind], '-', c=colors[ind])
        plt.plot(R[:,ind], Z[:,ind], '-', c=colors[ind])

    plt.axis((xmin, xmax, ymin, ymax))
    plt.gca().xaxis.set_major_locator(LinearLocator(numticks=numticks))
    plt.xlabel('R (m)')
    plt.ylabel('Z (m)')

    plt.savefig(figName+'.'+fileExt, bbox_inches='tight', dpi=dpi)
