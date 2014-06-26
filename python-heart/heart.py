#!/usr/bin/env python2
# Copyright (c) 2014 Joseph Wright <joegle@gmail.com>
# License: BSD 3 clause

import numpy as np
import serial
import sys
import time

class Heart_Monitor:
    def __init__(self,device="/dev/ttyUSB0"):
        """Initialize a new Heart_Monitor instance to read in newline delimited heart beat R wave intervals from 'device' which is usually a serial device but can also be stdin or file."""
        self.playback = 0 # True when reading from a file source
        self.stream  = device # data stream source

        try:
            self.stream = serial.Serial(device, 115200)
            sys.stderr.write("Connected to '%s' serial device\n" % (device))

        except TypeError:
            # for using using sys.stdin
            self.stream = device
            sys.stderr.write("Streaming data from '%s'\n" % device)

        except serial.serialutil.SerialException:
            self.stream = open(device, "r")
            sys.stderr.write("Streaming data from '%s'\n" % device)
            self.playback = 1

        except OSError:
            sys.stderr.write("Could not connect to '%s'\n" % device)
            raise

        self.RR_intervals = np.array([])
        self.beat_time = 0 #delay in ms from last last heart beat

        self.min_beat_time = 500 #threshold for detecting false beats from split error from ardiuno
        self.carry = 0

    def listen_for_beat(self):
        """Scan for next heart beat impulse newline print, corrects split beat error, append the IBI to the array"""

        try:
            raw_line = self.stream.readline()
            self.beat_time = int(str(raw_line))

            #Sometimes the arduino splits a heart beat, this combines the two halves if they appear faster than a threshold: self.min_beat_time
            if self.beat_time <= self.min_beat_time:
                if self.carry == 0:
                    self.carry = self.beat_time
                    return
                else:
                    self.beat_time += self.carry
                    self.carry = 0

            if self.playback:
                time.sleep(self.beat_time/1000.0)
            
        except ValueError as e:
            sys.stderr.write("Syncing with serial...\n")
            return

        except KeyboardInterrupt:
            sys.stderr.write("\nUser abort\n")
            self.on_quit()
            sys.exit()
         
        except Exception as e:
            sys.stderr.write("%s\n"%(e))
            raise

        self.RR_intervals = np.append(self.RR_intervals, self.beat_time)
        self.on_beat()
        return
        
    def on_beat(self):
        """Subroutine to run when heart beat is read"""
        print self.beat_time

    def start(self):
        """Begins the infinite loop of detecting heart beats"""
        sys.stderr.write("Starting monitor\n")
        while True:
            self.listen_for_beat()

    def on_quit(self):
        sys.stderr.write("Quitting monitor\n")

def main():
    session = Heart_Monitor()
    session.start()

if __name__ == "__main__":
    main()
