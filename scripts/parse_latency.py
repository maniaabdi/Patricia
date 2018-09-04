#!/usr/bin/python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import sys
import csv
import argparse

import matplotlib.pyplot as plt
import matplotlib
import numpy as np


# function for setting the colors of the box plots pairs
def setBoxColors(bp):
    plt.setp(bp['boxes'][0], color='blue')
    plt.setp(bp['caps'][0], color='blue')
    plt.setp(bp['caps'][1], color='blue')
    plt.setp(bp['whiskers'][0], color='blue')
    plt.setp(bp['whiskers'][1], color='blue')
#    plt.setp(bp['fliers'][0], color='blue')
#    plt.setp(bp['fliers'][1], color='blue')
    plt.setp(bp['medians'][0], color='blue')
    plt.setp(bp['boxes'][1], color='red')
    plt.setp(bp['caps'][2], color='red')
    plt.setp(bp['caps'][3], color='red')
    plt.setp(bp['whiskers'][2], color='red')
    plt.setp(bp['whiskers'][3], color='red')
 #   plt.setp(bp['fliers'][2], color='red')
 #   plt.setp(bp['fliers'][3], color='red')
    plt.setp(bp['medians'][1], color='red')


vanilla_lat_fn = sys.argv[1]
jaeger_lat_fn = sys.argv[2]

vanilla_lat_fn2 = sys.argv[3]
jaeger_lat_fn2 = sys.argv[4]

vanilla_lat_fn3 = sys.argv[5]
jaeger_lat_fn3 = sys.argv[6]


with open(vanilla_lat_fn, 'r') as vf, open(vanilla_lat_fn2, 'r') as vf2, open(vanilla_lat_fn3, 'r') as vf3, open(jaeger_lat_fn, 'r') as jf, open(jaeger_lat_fn2, 'r') as jf2, open(jaeger_lat_fn3, 'r') as jf3:
    v_rdr = csv.reader(vf, delimiter=',', quoting=csv.QUOTE_NONE)
    j_rdr = csv.reader(jf, delimiter=',', quoting=csv.QUOTE_NONE)

    v_rdr2 = csv.reader(vf2, delimiter=',', quoting=csv.QUOTE_NONE)
    j_rdr2 = csv.reader(jf2, delimiter=',', quoting=csv.QUOTE_NONE)

    v_rdr3 = csv.reader(vf3, delimiter=',', quoting=csv.QUOTE_NONE)
    j_rdr3 = csv.reader(jf3, delimiter=',', quoting=csv.QUOTE_NONE)



    v_lat = []
    j_lat = []

    v_lat2 = []
    j_lat2 = []

    v_lat3 = []
    j_lat3 = []




    for v_latl in v_rdr:
        print(int(v_latl[7].replace('\'', '').split('.')[1]))
        v_lat.append(float(v_latl[7].replace('\'', '').split(':')[2]))

    for j_latl in j_rdr:
        print(int(j_latl[7].replace('\'', '').split('.')[1]))
        j_lat.append(float(j_latl[7].replace('\'', '').split(':')[2]))


    for v_latl in v_rdr2:
        print(int(v_latl[7].replace('\'', '').split('.')[1]))
        v_lat2.append(float(v_latl[7].replace('\'', '').split(':')[2]))
    
    for j_latl in j_rdr2:
        print(int(j_latl[7].replace('\'', '').split('.')[1]))
        j_lat2.append(float(j_latl[7].replace('\'', '').split(':')[2]))


    for v_latl in v_rdr3:
        print(int(v_latl[7].replace('\'', '').split('.')[1]))
        v_lat3.append(float(v_latl[7].replace('\'', '').split(':')[2]))

    for j_latl in j_rdr3:
        print(int(j_latl[7].replace('\'', '').split('.')[1]))
        j_lat3.append(float(j_latl[7].replace('\'', '').split(':')[2]))


    fig, ax = plt.subplots(figsize=(5, 5))
#    plt.hold(True)
    matplotlib.rcParams.update({'font.size': 12})

    lat_128K = [v_lat2, j_lat2]
    lat_4K = [v_lat, j_lat]
    lat_1M = [v_lat3, j_lat3]

    # first boxplot pair
    bp1 = plt.boxplot(lat_4K, 1, '', positions = [1, 2], widths = 0.6)
    setBoxColors(bp1)

    # second boxplot pair
    bp2 = plt.boxplot(lat_128K, 1, '', positions = [4, 5], widths = 0.6)
    setBoxColors(bp2)

    # thrid boxplot pair
    bp3 = plt.boxplot(lat_1M, 1, '', positions = [7, 8], widths = 0.6)
    setBoxColors(bp3)

   
    # set axes limits and labels
#    plt.ylim(min(min(v_lat), min(j_lat)),max(max(v_lat), max(j_lat)))
    ax.set_xticklabels([' ', '4KB', '100KB', '1MB'])
    ax.set_xticks([0, 1.5, 4.5, 7.5])
    ax.get_yaxis().get_major_formatter().set_scientific(False)
    plt.ylim(0,0.2)   
    # draw temporary red and blue lines and use them to create a legend
    hB, = plt.plot([1,1],'b-')
    hR, = plt.plot([1,1],'r-')
    plt.legend((hB, hR),('Vanilla CEPH', 'w/ JAEGER CEPH'))
    hB.set_visible(False)
    hR.set_visible(False)

    plt.xlabel("Write Operation size")
    plt.ylabel("Write Operation Latency (second)")
    plt.subplots_adjust(left=0.20, bottom=0.16, right=0.98, top=0.94, wspace=None, hspace=None)
#    plt.legend(loc=2)
    fig.savefig('write_latency_boxplot_comparison.png')
    plt.show()
