# eMPTI experiment code

## Dependencies
We require browsertime. Install:

```
npm install browsertime
```

## Notes
- By default browsertime results will save in a `browsertime-results` directory. Be sure to move the results from a relay or non-relay run into their own respective directories once complete, e.g.:
    ```
    python browsertime_driver.py
    mv browsertime-results browsertime-results-no-relay
    
    ENABLE RELAY

    python browsertime_driver.py
    mv browsertime-results browsertime-results-relay
    ```

- tranco_list.txt is the top 1000 websites listed on the Tranco list as of January 27, 2023 

## Descriptions of Scripts

(1) DNS experiments
Script: plot_dns.py
Data: rtts_norelay.pickle, rtts_relay.pickle, rtts_google.pickle, rtts_cf.pickle, rtts_q9.pickle

(2) Page load experiments
Script: plot_plt.py
Data:
./browsertime-results-relay/*/*/browsertime.har
./browsertime-results-norelay/*/*/browsertime.har

(3) WebRTC experiments
- WebRTC: small-scale video conference
Script: plot_webrtc_small.py
Data: w-small.csv, wo-small.csv

- WebRTC: large-scale video conference
Script: plot_webrtc_large.py
Data: w-large.csv, wo-large.csv

(4) iPerf experiments
- Aggregated throughput
Script: plot_proxya_tput.py

- Fairness
Script: plot_proxya_fairness.py

- Proxy-A + fast user-space networking
Script: plot_bess_tput.py
