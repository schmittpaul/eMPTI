import subprocess
import pickle

rttdict = {}
with open('domain_set.pickle', 'rb') as handle:
  domains = pickle.load(handle)

for domain in domains:
  cmd = subprocess.Popen(
      'kdig -d @35.244.200.159 +tls-host=35.244.200.159 '
      +  #CHANGE TO WHATEVER IS NEEDED
      domain,
      shell=True,
      stdout=subprocess.PIPE)
  for line in cmd.stdout:
    line = line.decode("utf-8").strip()
    if ";; From" in line:
      rtt = line.split(" ")[-2]
      rttdict[domain] = rtt
      print(domain, rtt)

with open('rtts_CHANGEME.pickle', 'wb') as handle:
  pickle.dump(rttdict, handle, protocol=pickle.HIGHEST_PROTOCOL)