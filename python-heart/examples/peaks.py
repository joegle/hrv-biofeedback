#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal
import random

def fix(array):
    n = np.array([])
    for x in array:
        n = np.append(n, np.zeros((x-1)/100.0))
        n = np.append(n, [1])
    return n

best_files=["2015-04-28-18:10:13.txt","2015-06-18-20:52:08.txt","2015-05-26-10:19:14.txt","2015-04-29-15:10:18.txt","2015-04-25-19:00:26.txt", "2015-06-27-19:32:35.txt","2015-06-29-20:56:12.txt"]
#best_files=["2016-03-02-20:40:08.txt","2016-05-11-21:05:08.txt", "2016-03-13-20:00:24.txt","2016-06-21-18:13:49.txt"]
#sessions = open("files.list")
#files = []
#for line in sessions.readlines():
#    files.append(line.rstrip())

files = ["alice1.txt", "bob1.txt", "alice2.txt"]
for filename in files:
    #RR_intervals = np.loadtxt("../../data/"+file)
    RR_intervals = np.loadtxt(filename)
    RR_intervals = RR_intervals[RR_intervals < 2000]
    f, Pwelch_spec = signal.welch(fix(RR_intervals), 5, scaling='spectrum')

    print "+",filename, "len", len(Pwelch_spec)
    l_peak = signal.argrelmax(Pwelch_spec, order=2)[0]
    h_peak = signal.argrelmin(Pwelch_spec, order=2)[0]

    #print "l",l_peak
    #print "h",h_peak
    for x in l_peak:print f[x],Pwelch_spec[x]
    for x in range(1,6):
        print x,len(signal.argrelmin(Pwelch_spec, order=x)[0])

    # You can do regular plot or  
    #plt.semilogy(f, Pwelch_spec)
    plt.grid(True)
    
    plt.plot(f, Pwelch_spec, label='Model length'+filename)
    print 

plt.show()
