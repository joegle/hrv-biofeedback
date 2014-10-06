#!/usr/bin/env python2
import numpy as np
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import date2num
from matplotlib.ticker import MaxNLocator

# Scatter plot statistics of sessions 
#    ls ../data/* > files.txt
#    python2 stat_plotter.py

def process(filename,prefix=""):
    """return dict of statistics from heart rate interval file, use prefix to set directory path"""
    #print filename
    RR_intervals = np.loadtxt(prefix + filename)
    RR_intervals = RR_intervals[RR_intervals < 2000]

    a= np.mean(RR_intervals,dtype=np.float64)
    s= np.std(RR_intervals,dtype=np.float64)
    #print a
    return {"avg":a, "std":s}

    

f = open("files.txt","r")
dates = []
avg = []
std = []

# x = np.zeros((2,),dtype=('i4,f4,a10'))
for line in f.readlines():
    date_object = datetime.datetime.strptime(line, '%Y-%m-%d-%H:%M:%S.txt\n')
    dates.append(date_object)
    avg.append(60000/process(line.rstrip(), "../data/")["avg"] )   
    std.append(60000/process(line.rstrip(), "../data/")["std"] )   

dates_ar = np.array(dates)
fig, ax = plt.subplots()

#plt.plot(dates,avg,"bo")
plt.plot(dates,std,"ro")

datemin = datetime.date(dates_ar.min().year, 1, 1)
datemax = datetime.date(dates_ar.max().year,dates_ar.max().month+1, 1)
ax.set_xlim(datemin, datemax)

plt.grid(True)

#fig.autofmt_xdate()
#plt.gcf().autofmt_xdate()

#plt.title("Beats per minute of each Session")
plt.title("Standard Deviation of Heart Beat Intervals")
plt.ylabel("SD")
plt.xlabel("Date")
plt.show()

