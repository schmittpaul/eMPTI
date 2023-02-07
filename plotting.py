import matplotlib

matplotlib.use('Agg')

from matplotlib import pyplot as plt
from matplotlib import rc
import numpy as np
from cycler import cycler

# Set fonts to Helvetica
rc('font', **{
    'family': 'sans-serif',
    'sans-serif': ['Helvetica'],
    'size': '10'
})

# Set sane defaults
rc('figure', **{'figsize': ['3.64', '2.5']})
rc('legend', **{'fontsize': '8', 'fancybox': 'True'})
rc('axes', **{'linewidth': '0.5'})
rc('patch', **{'linewidth': '0.5'})
rc('grid', **{'linewidth': '0.25'})
rc('xtick', **{'major.width': '.25', 'minor.width': '.25'})
rc('ytick', **{'major.width': '.25', 'minor.width': '.25'})

# Disable type 3 fonts
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

# A colorblind-safe palette and linestyle cycler
line_cycler = (cycler(color=[
    "#348ABD", "#A60628", "#7A68A6", "#467821", "#E24A33", "#CF4457", "#188487"
]) + cycler(linestyle=["-", "--", "-.", ":", "-", "--", "-."]))

plt.rc('axes', prop_cycle=line_cycler)


# Simple CDF Plotting code
def cdf(x, plot=True, *args, **kwargs):
  x, y = sorted(x), np.arange(len(x)) / len(x)
  return plt.plot(x, y, *args, **kwargs) if plot else (x, y)