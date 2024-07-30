# ElectronRootOptimization
This repository contains files related to the paper "Direct optimization of neoclassical ion transport in stellarator reactors".

The configurations in the paper live as `wout` files in the `configurations/` subdirectory.

The scripts to create each figure in the paper live in the `figure*/` subdirectories.

The information in table 1 can be obtained from the NTSS files in the `figure5/` subdirectory with the exception of the mirror ratio, which can be obtained from the `wout` file in the `configurations/opt/` subdirectory.

The information in tables 2, 3, and 4 can be obtained from the `input.*` files in the `configurations/opt/` subdirectory.

All the figures in the paper created using Python can be reproduced by running `makeAllPlots.py`. (The figures for field strength on a flux surface and the maximum-$J$ property were produced by others.)
