# ElectronRootOptimization
This repository contains files related to the paper ["Direct optimization of neoclassical ion transport in stellarator reactors"](https://doi.org/10.1088/1741-4326/ad75a6).

The configurations in the paper live as `wout` files in the `configurations/` subdirectory.

The scripts to create each figure in the paper live in the `figure*/` subdirectories.

The information in table 1 can be obtained from the `input.*` files in the `configurations/opt/` subdirectory.

The information in table 2 can be obtained from the NTSS files in the `figure5/` subdirectory with the exception of the mirror ratio, which can be obtained from the `wout` file in the `configurations/opt/` subdirectory.

All the figures in the paper created using Python can be reproduced by running `makeAllPlots.py`. (The figures for field strength on a flux surface and the maximum $J$ property were produced by [Samuel Lazerson](https://scholar.google.com/citations?user=OJl6dcwAAAAJ&hl=en&oi=ao).)
