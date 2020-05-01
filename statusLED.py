from gpiozero import LED
from time import sleep
from gpiozero.pins.pigpio import PiGPIOFactory

class StatusLED:
    def __init__(self):
        robot_pins = PiGPIOFactory(host="192.168.1.22")
        self.led = LED(14, pin_factory=robot_pins)
    def blink(self):
        while True:
            self.led.on()
            sleep(.5)
            self.led.off()
            sleep(.5)
    def cleanUp(self):
        robot_pins = PiGPIOFactory(host="192.168.1.22")
        led = LED(14, pin_factory=robot_pins)
        led.on()
