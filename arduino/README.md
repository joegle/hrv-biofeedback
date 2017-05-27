# Arduino Firmware

The arduino runs a slightly modified version of the original Pulse Sensor Amped code at [pulsesensor.myshopify.com](http://pulsesensor.myshopify.com/pages/code-and-guide). It is modified to only send the IBI through the serial port.

There are two options for obtaining the firmware:

1. Makefile with c++ code and arduino core 
2. arduino_sketch/ project compiled and loaded with the [Arduino IDE](http://arduino.cc/en/Main/Software)

Run `make all` to compile c++ version of the firmware with the included arduino core libaries. 

This code has default configuration for standard Arduino Atmega328P chip. Configure the build process in `Makefile` variables.

## Resources

* https://github.com/WorldFamousElectronics/PulseSensor_Amped_Arduino/blob/master/README.md
* https://pulsesensor.com/pages/pulse-sensor-amped-arduino-v1dot1

> If you are using a FIO or LillyPad Arduino or Arduino Pro Mini 3V or Arduino SimpleSnap or other Arduino that has ATmega168 or ATmega328 with 8MHz oscillator, change the line TCCR2B = 0x06 to TCCR2B = 0x05.

> The only other thing you will need is the correct ISR vector in the next step. ATmega32u4 devices use ISR(TIMER1_COMPA_vect)

> PWM on pins 3 and 11 will not work when using this code, because we are using Timer 2! 🤷‍♂️🤷‍♀️

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
