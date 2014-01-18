# HRV biofeedback
[@joegle](https://twitter.com/Joegle) / [joegle.com](http://joegle.com)

Collection of programs (written mostly in Python2) I've made for collecting live heart beat signal and processing it, suitable for prototyping heart rate 
variability training applications.

Biofeedback is the process of gaining greater awareness of physiological functions primarily using instruments that provide information on the activity of those same systems, with a goal of being able to manipulate them at will.

## Links


## Heart beat hardware
The hardware setup consists of:

* Arduino Duemilanove microcontroller connected to Linux server with USB cord
* Pulse Sensor Amped running off 5V and connected to Analog In 0 pin
* Pulse Sensor clipped to ear lobe

## Software and Firmware
The Arduino is loaded with modified Pulse Sensor firmware.


## python-heart Module
The core of the server side data uplink is done with `heart.py` module depending on:

* pySerial
* NumPy

### Usage
```
import heart
monitor = heart.Heartbeat_Monitor("/dev/ttyUSB0")
monitor.start()
```

Or

```
$ python2 -m heart
```


# Tips
```sh
$ stty -F /dev/ttyUSB0 cs7 cstopb -ixon raw speed 115200```
$ cat /dev/ttyUSB0
```
