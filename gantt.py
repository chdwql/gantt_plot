# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 22:55:51 2017

@author: sd_wangql
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import cm
from datetime import datetime, timedelta
from matplotlib import rcParams
import matplotlib
import sys


def gantt(x1, x2, y, names):
    rcParams['font.sans-serif'] = ['STKaiti']

    labs = []
    tickloc = []
    col = []
    color = iter(cm.Dark2(np.linspace(0, 1, len(y))))

    # generate a line and line properties for each station
    plt.subplots(1, 1, figsize=(8, 2))
    ax = plt.subplot(1,1,1)
    for i in range(len(y)):
        c = next(color)
        plt.hlines(i+1, x1[i], x2[i], label=y[i], color=c, linewidth=8)
        labs.append(names[i].title())
        tickloc.append(i+1)
        col.append(c)
    plt.ylim(0, len(y)+1)
    plt.yticks(tickloc, labs)

    # create custom x labels
    ax.xaxis.set_major_locator(matplotlib.dates.YearLocator(base=1, month=1,day=1))
    ax.xaxis.set_minor_locator(matplotlib.dates.MonthLocator(interval=1))
    plt.xlim(datetime(np.min(x1).year,1,1), np.max(x2) + timedelta(days=180))
    plt.xlabel('Date')
    plt.ylabel('Station Names')
    plt.title('Timeline')
    plt.grid(axis='y', linestyle='dotted')

    # color y labels to match lines
    gytl = plt.gca().get_yticklabels()
    for i in range(len(gytl)):
        gytl[i].set_color(col[i])
    plt.tight_layout()
    plt.savefig('gantt.png', dpi=300)
    plt.close()


def main():
    data = pd.read_csv('example.txt', sep=' ', parse_dates=True)
    x1 = pd.to_datetime(data.start)
    x2 = pd.to_datetime(data.end)
    y = data.ind
    names = data.names
    gantt(x1, x2, y, names)


if __name__ == "__main__":
    sys.exit(main())
