from gpiozero import Servo
import time
from gpiozero.pins.pigpio import PiGPIOFactory

robot_pins = PiGPIOFactory(host="192.168.1.22")

servo1 = Servo(16, pin_factory=robot_pins)
servo4 = Servo(20, pin_factory=robot_pins)
servo5 = Servo(21, pin_factory=robot_pins)
servo3 = Servo(19, pin_factory=robot_pins)
servo2 = Servo(13, pin_factory=robot_pins)
servo6 = Servo(26, pin_factory=robot_pins)

servo1.value = 1
print("Servo 1")
time.sleep(1)
servo1.value = 0
time.sleep(.5)
servo2.value = 1
print("servo 2")
time.sleep(1)
servo2.value = 0
time.sleep(.5)
servo3.value = 1
print("Servo 3")
time.sleep(1)
servo3.value = 0
time.sleep(.5)
servo4.value = 1
print("Servo 4")
time.sleep(1)
servo4.value = 0
time.sleep(.5)
servo5.value = 1
print("Servo 5")
time.sleep(1)
servo5.value = 0
time.sleep(.5)
print("servo 6")
servo6.value = -1
time.sleep(1)
servo6.value = 0
