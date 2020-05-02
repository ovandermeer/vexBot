from debug import Debug
from gpiozero import Servo
from time import sleep
from gpiozero.pins.pigpio import PiGPIOFactory

robot_pins = PiGPIOFactory(host="192.168.1.22")

class ServoBot:
    def __init__(self,debug):
        self.debug = Debug.setDebug(debug)
        self.servo1 = Servo(16, pin_factory=robot_pins)
        self.servo2 = Servo(13, pin_factory=robot_pins)
        self.servo3 = Servo(19, pin_factory=robot_pins)
        self.servo4 = Servo(20, pin_factory=robot_pins)
        self.servo5 = Servo(21, pin_factory=robot_pins)
        self.servo6 = Servo(26, pin_factory=robot_pins)
        
    def move(self,m1,m2,m3,m4):
        self.servo1.value = m1
        self.servo2.value = m2
        self.servo3.value = m3
        self.servo4.value = m4
        
    def lift(self,m5,m6):
	    self.servo5.value = m5
	    self.servo6.value = m6

    def forward(self):
        Debug.message("forward",self.debug)
        self.move(1,-1,1,-1)
        #self.move(1,-1)
    def backward(self):
        Debug.message("backward",self.debug)
        self.move(-1,1,-1,1)
        
    def left(self):
        Debug.message("left",self.debug)
        self.move(-1,-1,-1,-1)
        
    def right(self):
        Debug.message("right",self.debug)
        self.move(1,1,1,1)
        
    def stop(self):
        Debug.message("stop",self.debug)
        self.move(0,0,0,0)
    def extend(self):
	    Debug.message("extending",self.debug)
	    self.lift(.7,-.7)
    def retract(self):
	    Debug.message("retracting",self.debug)
	    self.lift(-.7,.7)
    def liftStop(self):
	    Debug.message("Stopping lift",self.debug)
	    self.lift(0,0)
