#!/usr/bin/env python2
import heart
import matplotlib.pyplot as plt
import numpy as np

#TODO
# Epoch create epoch named file
# opt-parse

class feedback(heart.Heart_Monitor):
    def __init__(self,serial_device="/dev/ttyUSB0"):
        heart.Heart_Monitor.__init__(self,serial_device)

    def on_beat(self):
        self.plot()
        print self.beat_time
 
    def plot(self):
        fourier = np.fft.fft(self.RR_intervals)
        FFT = abs(fourier)
        freqs=np.fft.fftfreq(self.RR_intervals.size, d=1)
        FFT_inverse = np.fft.ifft(FFT)

        plt.cla()
        #plt.plot(freqs,np.log(FFT),'x')
        plt.plot(freqs,np.log(FFT_inverse),',')
        plt.draw()
        plt.pause(0.0001)


def main():
    session=feedback()
    session.start()

if __name__ == "__main__":
    main()
