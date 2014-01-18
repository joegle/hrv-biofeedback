# Arduino Firmware

The arduino runs a slightly modified version of the original Pulse Sensor Amped code at [pulsesensor.myshopify.com](http://pulsesensor.myshopify.com/pages/code-and-guide). It is modified to only send the IBI through the serial port.

There are two options for obtaining the firmware:

1. Makefile with c++ code and arduino core 
2. arduino_sketch/ project compiled and loaded with the [Arduino IDE](http://arduino.cc/en/Main/Software)

## Compile

Run `make all` to compile c++ version of the firmware with the included arduino core libaries. 

This code has default configuration for standard Arduino Atmega328P chip. Configure the build process in `Makefile` variables.

## Dependencies

* Arduino SDK (if using the sketch project)
* gcc-avr
* binutils-avr
* avr-libc
* avrdude

## Upload

Run `make upload` to upload the firmware into the USB connected Arduino.


## arduino_sketch/ for Arduino IDE

This folder has ino files that can be compiled with the [Arduino IDE](http://arduino.cc/en/Main/Software)
