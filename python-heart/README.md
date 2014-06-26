# python-heart

python-heart is a Python2 module that provides a class for reading live heart beat data from the bundled Arduino hrv-biofeedback firmware (see hrv-biofeedback/arduino/).

It provides a class for typical HRV biofeedback program setting up the serial connection and collecting the data into a NumPy array, etc.

## Dependencies

* pySerial
* NumPy

## Installation

To install the python module locally:
`python2 setup.py install --user`

## Usage
```
import heart
monitor = heart.Heartbeat_Monitor("/dev/ttyUSB0")
monitor.start()
```

The module provides the `Heartbeat_Monitor` class which requires one string argument of the location of your serial device. After `__init__` sets up IO the `start` method will begin the reading of heart beat pulses in the form of newline seperated integers milliseconds between heart beats coming from the Arduino:
```
624
636
610
598
614...
```

The `on_beat` callback will run each time a beat detected with access to the current `self.beat_time` and the `self.RR_intervals` NumPy containing the entire sequence of interbeat intervals from calling `start`.

The command line program `record.py` in the examples/ will setup a recording session and write the data to a timestamped file.

## Heart beat hardware
The hardware setup consists of:

* Arduino microcontroller connected to Linux server with USB cord
* Pulse Sensor Amped running off 5V and connected to Analog In 0 pin
* Pulse Sensor clipped to ear lobe
* Arduino loaded with modified Pulse Sensor firmware 