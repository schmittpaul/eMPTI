import matplotlib

matplotlib.use('Agg')

import argparse
from collections import Counter
import json
import glob
import os
import pickle
from matplotlib import pyplot as plt
import plotting
import numpy as np



## gcp
## tput
# bar_group = 3
# bar_indent = 0.02
# bar_width = 0.3
# x0 = np.arange(bar_group)
# x1 = [x + (bar_width + bar_indent) for x in x0]
# y0 = [1.74, 1.45, 4.11]
# y1 = [4.05, 2.60, 2.28]

## fariness
bar_group = 2
bar_indent = 0.04
bar_width = 0.3
x0 = np.arange(bar_group)
x1 = [x + (bar_width + bar_indent) for x in x0]
y0 = [0.999, 0.870]
y1 = [0.962, 0.926]

def main():
  plotting.bar(x0, y0, label="MPTI - Pre-Proxy", width = bar_width)
  plotting.bar(x1, y1, label="MPTI - Proxy-A", width = bar_width)
  # plotting.bar(x1, y1, label="No MPTI (direct)", width = bar_width)
  # for i, v in enumerate(y0):
  #     plt.text(x0[i], v, str(v), color='blue')

  # plt.xlim(50, 25000)
  # plt.xticks([0, 5000, 10000, 15000, 20000, 25000])
  if bar_group == 5:
    plt.xticks([r + bar_width for r in range(bar_group)], ['1000', '2500', '5000', '7500', '10000'])
  if bar_group == 3:
    plt.xticks([r + bar_width for r in range(bar_group)], ['1', '50', '500'])
  if bar_group == 2:
    plt.xticks([r + bar_width for r in range(bar_group)], ['50', '500'])
  # plt.yticks([0, .25, .5, .75, 1])
  # plt.xscale('symlog')
  plt.xlabel('Number of concurrent flows')
  # plt.ylabel('Aggregated tput (Gbps)')
  plt.ylabel('Fairness score')
  plt.grid()
  legend = plt.legend(loc='upper left')
  # legend.get_frame().set_alpha(None)
  # legend.get_frame().set_facecolor((0, 0, 1, 0.1))
  # plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0))
  plt.tight_layout()
  plt.savefig("preproxy-tput.pdf")

if __name__ == '__main__':
  main()
