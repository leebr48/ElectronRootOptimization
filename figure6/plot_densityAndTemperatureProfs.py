# Inputs
profsFilePaths = ['opt'] # Path to the main file. Auxiliary files (such as *_Dij) will also be loaded by the program.
figNamePrefixes = profsFilePaths
nMax = 2.0
TMax = 25.1
xSizeInches = 9
ySizeInches = 6
useRho = True

# Indices of relevant quantities - use the values listed in the file, they will be converted to Python indices automatically
mainInds = {
'r':1, # In m
'ne':2, # In 10^20 m^-3
'nD':3, # In 10^20 m^-3
'nT':4, # In 10^20 m^-3
'nHe':5, # In 10^20 m^-3
'Te':6, # In keV
'TD':7, # In keV
'TT':8, # In keV
'Er':9, # In kV/m
'p':11, # In Pa
'Ibs':63, # In A
'vaciota':69, # Uses susceptance matrices to exclude bootstrap current from the calculation, like vaciota in STELLOPT
'iota':70 # Uses susceptance matrices to include bootstrap current in the calculation
}

LInds = {
'r':1, # In m
'L11e':2, # In m^2/s
'L12e':3, # In m^2/s
'L11D':8, # In m^2/s
'L12D':9, # In m^2/s
'L11T':14, # In m^2/s
'L12T':15, # In m^2/s
'L11He':20, # In m^2/s
'L12He':21 # In m^2/s
}

################################################################
# Import necessary modules
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import sys
sys.path.append('../plotStandards')
from plotStandards import axisFontSize, legendFontSize, dpi, fileExt, colors

plt.rc('font', size=axisFontSize)
plt.rc('legend', fontsize=legendFontSize)

# Handy functions
def fixInd(ind):
    return ind - 1

def loadData(filePath, fileType='main'):
    global a
    if fileType == 'main':
        skiprows = 1
        inds = mainInds
    elif fileType == 'L':
        skiprows = 2
        inds = LInds
    else:
        raise IOError('Unkown fileType.')
    data = np.loadtxt(filePath, skiprows=skiprows)
    rInd = fixInd(inds['r'])
    a = np.max(data[:, rInd])
    return data

def loadVec(ind, fileType='main'):
    if fileType == 'main':
        return mainFilteredData[:, fixInd(ind)]
    elif fileType == 'L':
        return LFilteredData[:, fixInd(ind)]
    else:
        raise IOError('Unkown fileType.')

def my_formatter(x, pos):
    if x == 0:
        return str(int(0))
    elif x == 1:
        return str(int(1))
    else:
        return '{0:.1f}'.format(x)

def makePlot(xdata, ydata, ylabel, figName, leg=None, linestyles=None, fileExt=fileExt, yticks=None, ymin=None, ymax=None):
    formatter = FuncFormatter(my_formatter)
    plt.subplots(figsize=(xSizeInches, ySizeInches))
    for i in range(ydata.shape[1]):
        if linestyles is None:
            plt.plot(xdata[:, i], ydata[:, i], c=colors[i])
        else:
            plt.plot(xdata[:, i], ydata[:, i], linestyle=linestyles[i], c=colors[i])
    plt.xlim(xmin=np.min(xdata), xmax=np.max(xdata))
    plt.gca().xaxis.set_major_formatter(formatter)
    if ymin is not None:
        plt.ylim(ymin=ymin)
    if ymax is not None:
        plt.ylim(ymax=ymax)
    if yticks is not None:
        plt.yticks(np.arange(0, 25.1, yticks))
    plt.xlabel(xlab)
    plt.ylabel(ylabel)
    if leg is not None:
        plt.legend(leg, loc='best')
    box = mpl.transforms.Bbox.from_extents((-0.35, -0.35, xSizeInches-0.7, ySizeInches-0.5)) # (xmin, ymin, xmax, ymax)
    plt.savefig(figName+'.'+fileExt, bbox_inches=box, dpi=dpi)

def multiPlot(xdata, ydataList):
    y = np.column_stack(ydataList)
    x = np.tile(xdata, (y.shape[1],1)).T
    return x, y

def calcDelta12(species):
    L11 = 'L11' + species
    L12 = 'L12' + species
    return vecs[L12] / vecs[L11]

# Do work
for profsFilePath, figNamePrefix in zip(profsFilePaths, figNamePrefixes):

    # Load data
    mainFilteredData = loadData(profsFilePath, fileType='main')
    LFilteredData = loadData(profsFilePath + '_Dij', fileType='L')

    # Grab relevant variables
    vecs = {}
    for variable, index in mainInds.items():
        vecs[variable] = loadVec(index, fileType='main')
    for variable, index in LInds.items():
        vecs[variable] = loadVec(index, fileType='L')

    # Plot things
    if useRho:
        xData = vecs['r'] / a
        xlab = r'$\rho$'
    else:
        xData = vecs['r']
        xlab = r'$r$ (m)'

    stdLeg = ['e', 'D', 'T', 'He']
    stdStyle = ['solid', 'solid', 'dashed', 'dotted']

    makePlot(*multiPlot(xData, [vecs['ne'], vecs['nD'], vecs['nT'], vecs['nHe']]), r'Density ($10^{20}~\mathrm{m^{-3}}$)', figNamePrefix + '_n', leg=stdLeg, linestyles=stdStyle, ymin=0, ymax=nMax)
    makePlot(*multiPlot(xData, [vecs['Te'], vecs['TD'], vecs['TT'], vecs['TT']]), r'Temperature (keV)', figNamePrefix + '_T', leg=stdLeg, linestyles=stdStyle, yticks=5, ymin=0, ymax=TMax)
