#!/usr/bin/env python2
import heart
import redis
import numpy as np

#TODO
# Epoch create epoch named file
# opt-parse

class feedback(heart.Heart_Monitor):
    def __init__(self,serial_device="/dev/ttyUSB0"):
        heart.Heart_Monitor.__init__(self,serial_device)
        self.connection = redis.StrictRedis(host='localhost', port=6379, db=0) 

    def on_beat(self):
        self.redis_serve()
 
    def redis_serve(self):
        self.connection.set('beat',self.beat_time)
        self.connection.set('std10',round(np.std(self.RR_intervals[-10:])))
        self.connection.set('std50',round(np.std(self.RR_intervals[-50:])))
        self.connection.set('avg10',round(np.average(self.RR_intervals[-10:])))

def main():
    session=feedback()
    session.start()

if __name__ == "__main__":
    main()
