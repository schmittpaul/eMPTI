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

pltrelay = []
pltnorelay = []

def har_metrics(har):
  pages = {}
  for page in har["log"]["pages"]:
    try:
      name = page["id"]
      plt = page["pageTimings"]["onLoad"]
      # si = page["_visualMetrics"]["SpeedIndex"]
      # fp = page["pageTimings"]["_firstVisualChange"]
      # dom = page["pageTimings"]["_domContentLoadedTime"]

      server = None
      for d in har["log"]["entries"][0]["response"]["headers"]:
        if d["name"].lower() == "server":
          server = d["value"]

      pages[name] = Counter({
          # "si": si,
          "plt": plt,
          # "fp": fp,
          # "dom": dom,
          "server": server,
          "connections": Counter(),
          "domains": Counter()
      })

      for e in har["log"]["entries"]:
        if e["pageref"] == name:
          url = e["request"]["url"]
          size = e["response"]["bodySize"]
          connection = e["connection"]
          pages[name]["connections"][connection] += size

          domain = url.split("/")[2]
          pages[name]["domains"][domain] += size

          is_h3 = e["response"]["httpVersion"].startswith("h3-")
          is_h1 = e["response"]["httpVersion"] == "http/1.1"

          pages[name]["obj_nb"] += 1
          pages[name]["obj_sz"] += size

          if pages[name]["obj_nb"] == 1:
            pages[name]["status"] = e["response"]["status"]

          if is_h3:
            pages[name]["obj_h3_nb"] += 1
            pages[name]["obj_h3_sz"] += size

          if is_h1:
            pages[name]["obj_h1_nb"] += 1
            pages[name]["obj_h1_sz"] += size

          if e["timings"]["connect"] >= 0:
            pages[name]["conn_nb"] += 1

          mimeType = e["response"]["content"]["mimeType"]
          if mimeType == "application/javascript":
            mimeType = "text/javascript"
          if mimeType.startswith("text/"):
            if not mimeType=="text/html" and not mimeType=="text/css" and not mimeType=="text/javascript" and \
              not mimeType=="text/plain":
              mimeType = "text/other"
          else:
            mimeType = mimeType.split("/")[0]

          if mimeType == "":
            mimeType = "none"
          pages[name]["obj_mime_{}".format(mimeType)] += 1
    except Exception:
      continue

  return list(pages.values())


for site in glob.glob('./browsertime-results-relay/*/*/browsertime.har',
                      recursive=True):
  h = json.loads(open(site, "r").read())
  tmp = har_metrics(h)
  for run in tmp:
    try:
        pltrelay.append(run['plt'])
    except:
        continue

for site in glob.glob('./browsertime-results-norelay/*/*/browsertime.har',
                      recursive=True):
  h = json.loads(open(site, "r").read())
  tmp = har_metrics(h)
  for run in tmp:
    try:
      pltnorelay.append(run['plt'])
    except:
      continue

def main():
  print(sorted(pltrelay)[len(pltrelay)//2])
  print(sorted(pltnorelay)[len(pltnorelay)//2])

  plotting.cdf(pltrelay, label="MPTI Relay")
  plotting.cdf(pltnorelay, label="No MPTI Relay (direct)")

  plt.xlim(50, 25000)
  plt.xticks([0, 5000, 10000, 15000, 20000, 25000])
  plt.yticks([0, .25, .5, .75, 1])
  # plt.xscale('symlog')
  plt.xlabel('Page load time (ms)')
  plt.ylabel('CDF')
  plt.grid()
  plt.legend()
  plt.tight_layout()
  plt.savefig("residential_plt.pdf")

if __name__ == '__main__':
  main()
