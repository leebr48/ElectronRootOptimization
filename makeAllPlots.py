#!/usr/bin/python

import os
from inspect import getfile, currentframe

thisFile = os.path.abspath(getfile(currentframe()))
thisDir = os.path.dirname(thisFile)

print('Making figure 1.')
os.chdir(os.path.join(thisDir, 'figure1'))
os.system('python plot_customLPK.py')
print('Finished making figure 1.')

print('Making figure 2.')
os.chdir(os.path.join(thisDir, 'figure2'))
os.system('python plot_D11vsNu.py')
print('Finished making figure 2.')

print('Making figure 3.')
os.chdir(os.path.join(thisDir, 'figure3'))
os.system('python plot_epseffs.py')
print('Finished making figure 3.')

print('Making figure 4.')
os.chdir(os.path.join(thisDir, 'figure4'))
os.system('python plot_singleConfigurationProfs.py')
os.system('python plot_multipleConfigurationProfs.py')
print('Finished making figure 4.')
