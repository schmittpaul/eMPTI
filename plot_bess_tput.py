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

## cloudlab
# tput
x0 = [1000, 2500, 5000, 7500, 10000, 25000, 30000, 40000, 50000, 100000, 1000000]
y0 = [9.353, 9.380, 9.342, 9.327, 9.353, 9.297, 5.314, 3.423, 2.919, 2.059, 1.646]

def main():
  plotting.curve(x0, y0, 'o-', label="MPTI - Proxy-A")

  plt.xlim(900, 1100000)
  plt.xticks([1000, 5000, 10000, 15000, 20000, 25000])
  plt.yticks([0, 2.5, 5.0, 7.5, 10.0])
  plt.xscale('symlog')
  plt.xlabel('Number of concurrent flows')
  plt.ylabel('Throughput (Gbps)')

  style="Simple,head_length=8,head_width=8,tail_width=5"
  arrow = arrow = matplotlib.patches.FancyArrowPatch((100000,3.5), (100000,2.5), arrowstyle=style, color="black")

  plt.gca().add_patch(arrow)
  plt.annotate('Out of L4 Ports', xy=(80000,2.7), xytext=(80000, 3.7))
  plt.grid()
  plt.legend(loc='lower left', framealpha=0.8)
  plt.tight_layout()
  plt.savefig("proxya-tput-cloudlab.pdf")
  return

if __name__ == '__main__':
  main()
