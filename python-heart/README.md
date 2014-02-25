# HRV biofeedback
@joegle

Collection of programs (written mostly in Python2) I've made for collecting live heart beat signal and processing it. Very suitible for prototyping with

Biofeedback is the process of gaining greater awareness of many physiological functions primarily using instruments that provide information on the activity of those same systems, with a goal of being able to manipulate them at will.

LINKs

# Install


## Heart beat hardware
The hardware setup consists of:

* Arduino Duemilanove microcontroller connected to Linux server with USB cord
* Pulse Sensor Amped running off 5V and connected to Analog In 0 pin
* Pulse Sensor clipped to ear lobe

### Pitfalls

* Cold temperatures will reduce circulation in ears and prevent heart beat detection through Pulse Sensor
* Add your username to the `uucp` group to have access to serial device or `tty`


## Software and Firmware
The Arduino is loaded with modified Pulse Sensor firmware.

## capture.py Module
The core of the server side data uplink is done with `capture.py` module depending on:

* pySerial
* NumPy

### Usage
```
import capture
monitor = capture.Heartbeat_Monitor("/dev/ttyUSB0")
monitor.start()
```

Install


# Tips
```sh
$ stty -F /dev/ttyUSB0 cs7 cstopb -ixon raw speed 115200```
$ cat /dev/ttyUSB0
```