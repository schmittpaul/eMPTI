import matplotlib

matplotlib.use('Agg')

import argparse
import os
import pickle
from matplotlib import pyplot as plt
# from matplotlib import rc
import numpy as np
# from cycler import cycler
import plotting

# # Set fonts to Helvetica
# rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica']})
# # Avoid type 3 fonts
# matplotlib.rcParams['pdf.fonttype'] = 42
# matplotlib.rcParams['ps.fonttype'] = 42

# # A colorblind-safe palette and linestyle cycler
# line_cycler = (cycler(color=[
#     "#E69F00", "#56B4E9", "#009E73", "#0072B2", "#CC79A7", "#D55E00", "#F0E442"
# ]) + cycler(linestyle=["-", "--", "-.", ":", "-", "--", "-."]))

# plt.rc('axes', prop_cycle=line_cycler)

relay = []
norelay = []
google = []
cf = []
q9 = []

# def cdf(x, plot=True, *args, **kwargs):
#   x, y = sorted(x), np.arange(len(x)) / len(x)
#   return plt.plot(x, y, *args, **kwargs) if plot else (x, y)


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('-d',
                      '--read_directory',
                      help='Read output files from given directory',
                      default='USC-runs')
  args = parser.parse_args()

  os.chdir(args.read_directory)

  with open('rtts_norelay.pickle', 'rb') as handle:
    norelaydict = pickle.load(handle)

  with open('rtts_relay.pickle', 'rb') as handle:
    relaydict = pickle.load(handle)

  with open('rtts_google.pickle', 'rb') as handle:
    googledict = pickle.load(handle)

  with open('rtts_cf.pickle', 'rb') as handle:
    cfdict = pickle.load(handle)

  with open('rtts_q9.pickle', 'rb') as handle:
    q9dict = pickle.load(handle)

  for key, val in relaydict.items():
    relay.append(float(val))

  for key, val in norelaydict.items():
    norelay.append(float(val))

  for key, val in googledict.items():
    google.append(float(val))

  for key, val in cfdict.items():
    cf.append(float(val))

  for key, val in q9dict.items():
    q9.append(float(val))

  plotting.cdf(relay, label="Relay")
  plotting.cdf(norelay, label="No Relay (direct)")
  plotting.cdf(google, label="Google")
  plotting.cdf(cf, label="Cloudflare")
  plotting.cdf(q9, label="Quad9")

  plt.xlim(0, 1700)
  plt.yticks([0, .25, .5, .75, 1])
  plt.xscale('symlog')
  plt.xlabel('DNS resolution time (ms)')
  plt.ylabel('CDF')
  plt.grid()
  plt.legend()
  plt.tight_layout()
  plt.savefig("dns.pdf")


if __name__ == '__main__':
  main()
