#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 12:41:28 2023
Winnpeg Transit file name: 'on_time_performance_2021_08.zip'
http://wpgopendata.blob.core.windows.net/transit-on-time-archive/on_time_performance_2021_08.zip
Only the 'Weekday' data from 2021-08-03T12:57:00 to 2021-08-03T16:44:29 is taken for analysis.

@author: mukeshgupta
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file = pd.read_excel(r'/Users/mukeshgupta/Documents/assignment/testdata.xlsx')
stime = file['Scheduled Time'].tolist()
deviation = file['Deviation'].tolist()
pos = np.arange(len(stime))

early=[i for i in deviation if i>0] 
late = [i for i in deviation if i<0]
ontime = [i for i in deviation if i==0]
prcnt_late = 100 * len(late)/len(deviation)
prcnt_early = 100 * len(early)/len(deviation)
prcnt_ontime = 100 * len(ontime)/len(deviation)

plt.figure(figsize=(10, 5))
plt.subplot(2,1,1)
plt.plot(deviation, "k", linestyle='-.')
plt.xlabel("Scheduled Time Sequence", fontsize=12)
plt.ylabel("Deviation (s)", fontsize=12)
plt.title('Winnipeg Transit Arrivals on a Weekday')

colors = ['g' if e>= 0 else 'r' for e in deviation]
ax = plt.subplot(2,1,2)
ax.bar(pos, deviation, width=1, color=colors)
plt.xlabel("Scheduled Time Sequence", fontsize=12)
plt.ylabel("Deviation (s)", fontsize=12)
plt.text(20, -200, "73% Late arrivals (Red)", fontsize=12)
plt.text(60, 100, "25% Early arrivals (Green)", fontsize=12)
plt.text(0, 150, "2% On-time arrivals", fontsize=12)
plt.tight_layout()

plt.savefig('Fig1.png', format = 'png', bbox_inches = 'tight', dpi = 300, \
              pad_inches = 0.1, transparent=False)