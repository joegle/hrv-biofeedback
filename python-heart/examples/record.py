#!/usr/bin/env python2
from __future__ import print_function
import heart
import datetime
import time
import sys
import numpy as np

class recorder(heart.Heart_Monitor):
    """Command line tool that records the Arduino heart beat data into timestamped file"""

    def __init__(self,serial_device="/dev/ttyUSB0"):
        heart.Heart_Monitor.__init__(self,serial_device)
        now = datetime.datetime.now()
        start_time = now.strftime('%Y-%m-%d-%H:%M:%S')
        self.datafile = open(start_time+".txt","w")
        print("Writing data to '%s'" % (self.datafile.name))
        #self.datafile.write("# %s"%(start_time))
        self.datafile.write("# R wave intervals in milliseconds per line\n")

    def start(self):
        """Begins the infinite loop of detecting heart beats"""
        sys.stderr.write("Starting monitor (Control-C to quit)\n")
        self.datafile.write("# start time: %s, %s\n"%(datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S'),time.time()))
        while True:
            self.listen_for_beat()

    def on_beat(self):
        #self.stream.write(chr(self.beat_time%255))
        print(self.beat_time, file=self.datafile)
        print(".", end="")
        sys.stdout.flush()

    def session_summary(self):
        print("\n= Session Summary =")
        print("File:", self.datafile.name)
        print(len(self.RR_intervals), "Beats")
        print(np.sum(self.RR_intervals), "ms total")
        print(60000/np.average(self.RR_intervals), "BPM")

    def on_quit(self):
        self.datafile.write("# end time: %s, %s\n"%(datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S'),time.time()))
        sys.stderr.write("Quitting monitor\n") 
        self.session_summary()
        self.datafile.close()

def main():
    session = recorder()
    session.start()

if __name__ == "__main__":
    main()

