#!/usr/bin/python

import os
from inspect import getfile, currentframe

thisFile = os.path.abspath(getfile(currentframe()))
thisDir = os.path.dirname(thisFile)

print('Making plots for figure 1.')
os.chdir(os.path.join(thisDir, 'figure1'))
os.system('python plot_pressure.py')
print('Finished making plots for figure 1.')

print('Making plots for figure 2.')
os.chdir(os.path.join(thisDir, 'figure2'))
os.system('python plot_customLPK.py')
print('Finished making plots for figure 2.')

print('Making plots for figure 3.')
os.chdir(os.path.join(thisDir, 'figure3'))
os.system('python plot_D11vsNu.py')
print('Finished making plots for figure 3.')

print('Making plots for figure 4.')
os.chdir(os.path.join(thisDir, 'figure4'))
os.system('python plot_epseffs.py')
print('Finished making plots for figure 4.')

print('Making plots for figure 5.')
os.chdir(os.path.join(thisDir, 'figure5'))
os.system('python plot_densityAndTemperatureProfs.py')
os.system('python plot_otherProfs.py')
print('Finished making plots for figure 5.')
