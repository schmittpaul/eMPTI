import subprocess
import pickle
from tqdm import tqdm

rttdict = {}
with open('domain_set.pickle', 'rb') as handle:
  domains = pickle.load(handle)

for domain in tqdm(domains):
  cmd = subprocess.Popen(
      'kdig -d @149.248.212.154 +tls-host=35.244.200.159 '  # no relay
      # 'kdig -d @35.244.200.159 +tls-host=35.244.200.159 ' # relay
      # 'kdig -d @8.8.8.8 +tls-host=8.8.8.8 ' # google
      # 'kdig -d @1.1.1.1 +tls-host=1.1.1.1 ' # cf
      # 'kdig -d @9.9.9.9 +tls-host=9.9.9.9 ' # q9
      +  #CHANGE TO WHATEVER IS NEEDED 149.248.212.154
      domain,
      shell=True,
      stdout=subprocess.PIPE)
  for line in cmd.stdout:
    line = line.decode("utf-8").strip()
    if ";; From" in line:
      rtt = line.split(" ")[-2]
      rttdict[domain] = rtt
      # print(domain, rtt)

with open('rtts_norelay.pickle', 'wb') as handle:
  pickle.dump(rttdict, handle, protocol=pickle.DEFAULT_PROTOCOL)