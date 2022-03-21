import os
import sys
import time

class e_paper_config:
    # GPIO Pins definition
    RST_PIN         = 17
    DC_PIN          = 25
    CS_PIN          = 8
    BUSY_PIN        = 24

    def __init__(self):
        import spidev
        import RPi.GPIO

        self.GPIO = RPi.GPIO

        self.SPI = spidev.SpiDev(0, 0)

    def digitalwrite(self, pin, value):
        self.GPIO.output(pin, value)

    def digitalread(self, pin):
        return self.GPIO.input(pin)

    def delay(self, delaytime): # delay in millisecond
        time.sleep(delaytime / 1000.0)

    def spi_writebyte(self, data):
        self.SPI.writebytes(data)

    def module_init(self):
        self.GPIO.setmode(self.GPIO.BCM)
        self.GPIO.setwarnings(False)
        self.GPIO.setup(self.RST_PIN, self.GPIO.OUT)
        self.GPIO.setup(self.DC_PIN, self.GPIO.OUT)
        self.GPIO.setup(self.CS_PIN, self.GPIO.OUT)
        self.GPIO.setup(self.BUSY_PIN, self.GPIO.IN)
        self.SPI.max_speed_hz = 4000000
        self.SPI.mode = 0b00
        return 0

    def exit(self):
        self.SPI.close()
        self.GPIO.output(self.RST_PIN, 0)
        self.GPIO.output(self.DC_PIN, 0)
        self.GPIO.cleanup()
        
