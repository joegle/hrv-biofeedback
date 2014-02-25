#!/usr/bin/env python2
from __future__ import print_function
import heart
import datetime
import time
import sys
import numpy as np
from subprocess import call


class feedback(heart.Heart_Monitor):
    def __init__(self,serial_device="/dev/ttyUSB0"):
        heart.Heart_Monitor.__init__(self,serial_device)
        now = datetime.datetime.now()
        start_time = now.strftime('%Y-%m-%d-%H:%M:%S')
        self.datafile = open(start_time+".txt","w")
        #self.datafile.write("# %s"%(start_time))
        self.datafile.write("# R wave intervals in milliseconds per line\n")

    def start(self):
        """Begins the infinite loop of detecting heart beats"""
        sys.stderr.write("Starting monitor\n")
        self.datafile.write("# start time: %s, %s\n"%(datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S'),time.time()))
        while True:
            self.listen_for_beat()

    def on_beat(self):

        print(self.beat_time, file=self.datafile)
        print(".", end="")
        sys.stdout.flush()

    def on_quit(self):
        self.datafile.write("# end time: %s, %s\n"%(datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S'),time.time()))
        self.datafile.close()
        sys.stderr.write("Quitting monitor\n") 

def main():
    session=feedback()
    session.start()

if __name__ == "__main__":
    main()
