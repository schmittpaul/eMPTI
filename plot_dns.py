import matplotlib
matplotlib.use('Agg')

from collections import Counter
import json
import glob
import seaborn as sns
from matplotlib import pyplot as plt
import pickle

relay = []
norelay = []

with open('rtts_norelay.pickle', 'rb') as handle:
  norelaydict = pickle.load(handle)

with open('rtts_relay.pickle', 'rb') as handle:
  relaydict = pickle.load(handle)

# print(relaydict)
for key, val in relaydict.items():
  relay.append(val)

for key, val in norelaydict.items():
  norelay.append(val)

sns.kdeplot(data=norelay, cumulative=True, label="No Relay")
sns.kdeplot(data=relay, cumulative=True, label="Relay")
# plt.xlim(0, 26000)
plt.xlabel('DNS resolution time (ms)')
plt.grid()
plt.legend()
plt.savefig("dns.pdf")