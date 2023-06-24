import matplotlib
matplotlib.use('Agg')

import argparse
from collections import Counter
import csv
from matplotlib import pyplot as plt
import plotting

def parse_csv_file(filename):
    data = []
    with open(filename, mode='r', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            rtt = float(row[0])
            jitter = float(row[1])
            loss = float(row[2])
            data.append((rtt, jitter, loss))
            if len(data) == 240:
                break
        print(f'Processed {len(data)} lines.')
    return data

def calc_mos(rtt, jitter, loss):
    ertt = rtt + jitter * 2
    r = 93 - ertt - loss
    r = max(r, 60)
    r = min(r, 100)
    mos = (r - 60) * (100 - r) * 0.000007 * r + 0.035 * r + 1
    return mos

def main():
    marker_size = 1.5
    line_width = 1

    time = [15 * i for i in range(240)]
    preproxy_data = parse_csv_file("w-small.csv")
    preproxy_rtt = [x[0] for x in preproxy_data]
    preproxy_jitter = [x[1] for x in preproxy_data]
    preproxy_loss = [x[2] * 100 for x in preproxy_data]
    preproxy_mos = [calc_mos(preproxy_rtt[i], preproxy_jitter[i], preproxy_loss[i]) for i in range(240)]

    direct_data = parse_csv_file("wo-small.csv")
    direct_rtt = [x[0] for x in direct_data]
    direct_jitter = [x[1] for x in direct_data]
    direct_loss = [x[2] * 100 for x in direct_data]
    direct_mos = [calc_mos(direct_rtt[i], direct_jitter[i], direct_loss[i]) for i in range(240)]

    print(sum(preproxy_rtt)/len(preproxy_rtt), sum(direct_rtt)/len(direct_rtt), sum(preproxy_rtt)/len(preproxy_rtt) - sum(direct_rtt)/len(direct_rtt))
    print(sum(preproxy_jitter)/len(preproxy_jitter), sum(direct_jitter)/len(direct_jitter))
    print(sum(preproxy_loss)/len(preproxy_loss), sum(direct_loss)/len(direct_loss))
    print(sum(preproxy_mos)/len(preproxy_mos), sum(direct_mos)/len(direct_mos))

    fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, sharex=True)
    ax1.plot(time, preproxy_rtt, 'o--', markersize=marker_size, linewidth=line_width, label="MPTI")
    ax1.plot(time, direct_rtt, 'x-.', markersize=marker_size, linewidth=line_width, label="No MPTI (direct)")
    ax1.set_ylabel("RTT (ms)", fontsize=7)
    ax1.set_xlim(0, 3600)
    ax1.set_ylim(0, 10)
    ax1.grid()

    ax1.legend(loc='upper right')

    ax2.plot(time, preproxy_jitter, 'o--', markersize=marker_size, linewidth=line_width, label="MPTI")
    ax2.plot(time, direct_jitter, 'x-.', markersize=marker_size, linewidth=line_width, label="No MPTI (direct)")
    ax2.set_ylabel("Jitter (ms)", fontsize=7)
    ax2.set_xlim(0, 3600)
    ax2.set_ylim(0, 25)
    ax2.grid()

    ax3.plot(time, preproxy_loss, 'o--', markersize=marker_size, linewidth=line_width, label="MPTI")
    ax3.plot(time, direct_loss, 'x-.', markersize=marker_size, linewidth=line_width, label="No MPTI (direct)")
    ax3.set_ylabel("Loss (%)", fontsize=7)
    ax3.set_xlim(0, 3600)
    ax3.set_ylim(0, 0.5)
    ax3.grid()

    ax4.plot(time, preproxy_mos, 'o--', markersize=marker_size, linewidth=line_width, label="MPTI")
    ax4.plot(time, direct_mos, 'x-.', markersize=marker_size, linewidth=line_width, label="No MPTI (direct)")
    ax4.set_ylabel("MOS", fontsize=7)
    ax4.set_xlim(0, 3600)
    ax4.set_ylim(3, 5)
    ax4.grid()

    plt.xlabel('Time (s)')
    fig.tight_layout()
    fig.savefig("webrtc-small-rtt.pdf")
    return

if __name__ == "__main__":
    main()
