CC=avr-gcc
CXX=avr-g++
AR=avr-ar
CHIP=atmega328p
MCU=-mmcu=$(CHIP)
CPU_SPEED=-DF_CPU=16000000UL
LIBS=-Ilib
CFLAGS=$(MCU) $(CPU_SPEED) -Os -w -ffunction-sections -fdata-sections -fno-exceptions $(LIBS)

SERIAL=/dev/ttyUSB0
BAUD=57600

OBJS = WInterrupts.o wiring_analog.o wiring.o wiring_digital.o wiring_pulse.o wiring_shift.o CDC.o HardwareSerial.o HID.o IPAddress.o main.o new.o Print.o Stream.o Tone.o USBCore.o WMath.o WString.o

libarduino.a: $(foreach obj,$(OBJS),build/$(obj))
	$(AR) crs libarduino.a build/*

build/%.o: lib/%.c
	@mkdir -p build
	$(CC) $< $(CFLAGS) -c -o $@ 

build/%.o: lib/%.cpp
	@mkdir -p build
	$(CXX) $< $(CFLAGS) -c -o $@ 

pulse.o: src/pulse.cpp
	@echo src/pulse.cpp
	$(CXX) $(CFLAGS)  -c $^ -o $@ 

firmware.elf: pulse.o libarduino.a
	@echo Linking firmware.elf
	$(CC) $(CFLAGS) -o $@ $^

firmware.hex: firmware.elf
	@echo Converting to firmware.hex
	avr-objcopy -O ihex -R .eeprom $^ $@

upload: firmware.hex
	avrdude -V -F -carduino -p$(CHIP)  -b$(BAUD) -P$(SERIAL) -D -U flash:w:$^:i

all: firmware.hex pulse.o libarduino.a
	@echo "SUCCESS!"
	@echo "To load run: 'make upload'"
	@true

clean:
	rm *o
	rm *hex
	rm *a
	rm -r build
	rm *elf
