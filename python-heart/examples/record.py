#!/usr/bin/env python2
from __future__ import print_function
import heart
import datetime
import time
import sys
import numpy as np
import argparse
import os
import stat

class recorder(heart.Heart_Monitor):
    """Command line tool that records the Arduino heart beat data into timestamped file"""

    def __init__(self, args):
        heart.Heart_Monitor.__init__(self,args.source)
        now = datetime.datetime.now()
        
        start_time = now.strftime('%Y-%m-%d-%H:%M:%S')
        stat_mode = os.stat(args.source).st_mode
        if stat.S_ISREG(stat_mode) or args.test:
            print("TESTING Not writing data to anywhere")
            self.datafile = open("/dev/null","w")
        else:
            self.datafile = open(start_time+".txt","w")
            print("Writing data to '%s'" % (self.datafile.name))
        
        #self.datafile.write("# %s"%(start_time))
        self.datafile.write("# R wave intervals in milliseconds per line\n")
        if args.message:
            self.log("annotation: " + args.message)

    def fifteen(self):
        # Fifteen minute mark
        print("$",end='')
        
    def log(self, message):
        self.datafile.write("# %s\n"%(message))
        
    def start(self):
        """Begins the infinite loop of detecting heart beats"""
        sys.stderr.write("Starting monitor (Control-C to quit)\n")
        self.datafile.write("# start time: %s, %s\n"%(datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S'),time.time()))
        while True:
            self.listen_for_beat()

    def on_beat(self):
        #self.stream.write(chr(self.beat_time%255))
        print(self.beat_time, file=self.datafile)
        char = "."
        
        if np.sum(self.RR_intervals)/60000 >= 15:
            char = '$'
        
        print(char, end="")
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


parser = argparse.ArgumentParser(description='Record heart beat intervals')

parser.add_argument('-m','--message', help='Log a message')
parser.add_argument('-t','--test', help="Test run", action='store_true')
parser.add_argument('source',help="Input source") # nargs='*' use '*' for 0 or more use '+' for 1 or more args (instead of 0 or more)

#        serial_device="/dev/ttyUSB0"
args = parser.parse_args()


def main():
    session = recorder(args)
    session.start()

if __name__ == "__main__":
    main()

