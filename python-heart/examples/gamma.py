#!/usr/bin/env python2
import heart
import numpy as np
from subprocess import call

class feedback(heart.Heart_Monitor):
    def __init__(self,serial_device="/dev/ttyUSB0"):
        heart.Heart_Monitor.__init__(self,serial_device)

    def on_beat(self):
        call(["xgamma","-ggamma",str((np.std(self.RR_intervals[-10:])/24))]) #gamma 0..10
        print self.beat_time
 

def main():
    session=feedback()
    session.start()

if __name__ == "__main__":
    main()
