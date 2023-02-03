import matplotlib

matplotlib.use('Agg')

from collections import Counter
import json
import glob
import seaborn as sns
from matplotlib import pyplot as plt
import pickle
import numpy as np

relay = []
norelay = []
google = []
cf = []
q9 = []


def cdf(x, plot=True, *args, **kwargs):
  x, y = sorted(x), np.arange(len(x)) / len(x)
  return plt.plot(x, y, *args, **kwargs) if plot else (x, y)


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

print(np.median(norelay))
print(np.median(relay))

cdf(relay, label="relay")
cdf(norelay, label="no relay")
cdf(google, label="Google")
cdf(cf, label="Cloudflare")
cdf(q9, label="Quad9")

plt.xlim(0, 1500)
plt.yticks([0, .25, .5, .75, 1])
plt.xscale('symlog')
plt.xlabel('DNS resolution time (ms)')
plt.grid()
plt.legend()
plt.savefig("dns.pdf")