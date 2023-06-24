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
# tput
bar_group = 3
bar_indent = 0.02
bar_width = 0.29
x0 = np.arange(bar_group)
x1 = [x + (bar_width + bar_indent) for x in x0]
x2 = [x + (bar_width + bar_indent) for x in x1]
y0 = [4.05, 2.60, 2.28]
y1 = [5.91, 6.67, 6.78]
y2 = [1.74, 1.45, 4.11]

def main():
  plotting.bar(x0, y0, label="MPTI - Proxy-A", width = bar_width)
  plotting.bar(x1, y1, label="No MPTI (direct)", width = bar_width)
  plotting.bar(x2, y2, label="MPTI - Pre-Proxy", width = bar_width)
  # for i, v in enumerate(y0):
  #     plt.text(x0[i], v, str(v), color='blue')

  # plt.xlim(50, 25000)
  plt.xticks([r + bar_width for r in range(bar_group)], ['1', '50', '500'])
  # plt.yticks([0, .25, .5, .75, 1])
  # plt.xscale('symlog')
  plt.xlabel('Number of concurrent flows')
  plt.ylabel('Throughput (Gbps)')
  plt.grid()
  legend = plt.legend(loc='lower right', framealpha=0.6)
  # legend.get_frame().set_alpha(None)
  # legend.get_frame().set_facecolor((0, 0, 1, 0.1))
  # plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0))
  plt.tight_layout()
  plt.savefig("proxya-tput-gcp.pdf")

if __name__ == '__main__':
  main()
