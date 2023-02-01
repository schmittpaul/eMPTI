from collections import Counter
import json
import glob
import pickle

pltrelay = []
pltnorelay = []


def har_metrics(har):
  dom = set()
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
      for dmnname in pages[name]["domains"]:
        dom.add(dmnname)
    except Exception:
      continue

  return dom


alldomains = set()
relaydomains = set()
norelaydomains = set()

for site in glob.glob('./browsertime-results-relay/*/*/browsertime.har',
                      recursive=True):
  h = json.loads(open(site, "r").read())
  relaydomains.update(har_metrics(h))

alldomains.update(relaydomains)

for site in glob.glob('./browsertime-results-norelay/*/*/browsertime.har',
                      recursive=True):
  h = json.loads(open(site, "r").read())
  norelaydomains.update(har_metrics(h))

alldomains.update(norelaydomains)

print(len(relaydomains), len(norelaydomains), len(alldomains))
with open('domain_set.pickle', 'wb') as handle:
  pickle.dump(alldomains, handle, protocol=pickle.DEFAULT_PROTOCOL)
