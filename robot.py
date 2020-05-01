from debug import Debug
import RPi.GPIO as IO
from time import sleep
from evdev import InputDevice, categorize, ecodes
from gpiozero.pins.pigpio import PiGPIOFactory

class Robot:
    def __init__(self,debug):
        self.debug = Debug.setDebug(debug)
        
        robot_pins = PiGPIOFactory(host="192.168.1.28")
        
        Debug.message("setting up robot",self.debug)
        #setup board
        IO.setwarnings(False)
        IO.setmode(IO.BCM)
        #initiate robot motors
        dmp1 = 13      #Drive Motor Pin 1
        dmp2 = 12      #Drive Motor Pin 2
        dmp3 = 17      #Drive Motor Pin 3
        dmp4 = 27      #drive Motor Pin 4
        #initiate pins
        IO.setup(dmp1,IO.OUT)
        IO.setup(dmp2,IO.OUT)
        IO.setup(dmp3,IO.OUT)
        IO.setup(dmp4,IO.OUT)
        #set the PMW frequency for the Vex 29 Motor Controllers at 50Hz
        self.dm1 = IO.PWM(dmp1,50)     #Drive Motor 1
        self.dm2 = IO.PWM(dmp2,50)     #Drive Motor 2
        self.dm3 = IO.PWM(dmp3,50)     #Drive Motor 3
        self.dm4 = IO.PWM(dmp4,50)     #Drive Motor 4
        #initiate motors at 0 so they are stopped when program starts
        self.dm1.start(0)
        self.dm2.start(0)
        self.dm3.start(0)
        self.dm4.start(0)
    
    def move(self,m1,m2,m3,m4):
        self.dm1.ChangeDutyCycle(m1)
        self.dm2.ChangeDutyCycle(m2)
        self.dm3.ChangeDutyCycle(m3)
        self.dm4.ChangeDutyCycle(m4)
        
    def forward(self,speed):
        Debug.message("forward",self.debug)
        if(speed == 1):
            self.move(8,8,8,8)
        elif(speed == 2):
            self.move(9,9,9,9)
        elif(speed == 3):
            self.move(10,10,10,10)
            
    def backward(self,speed):
        Debug.message("backward",self.debug)
        if(speed == 1):
            self.move(5,5,5,5)
        elif(speed == 2):
            self.move(6,6,6,6)
        elif(speed == 3):
            self.move(7,7,7,7)

    def right(self):
        Debug.message("right",self.debug)
        self.move(6,6,9,9)
    
    def left(self):
        Debug.message("left",self.debug)
        self.move(9,9,6,6)
        
    def stop(self):
        Debug.message("stop",self.debug)
        self.move(0,0,0,0)
