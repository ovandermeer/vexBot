from debug import Debug
from gpiozero import LED
from servoBot import ServoBot
from gamePad import GamePad
from action import Action
from time import sleep
from statusLED import StatusLED
from gpiozero.pins.pigpio import PiGPIOFactory
import threading
from pygame import mixer

robot_pins = PiGPIOFactory(host="192.168.1.22")


class Main:
    def initialize(self):
        self.debug = True
        self.bot = ServoBot(self.debug)
        self.controller = GamePad(self.debug)
        self.action = Action(self.bot,self.debug, self)
        mixer.init()
        print("init")
        mixer.music.load("/home/pi/Desktop/Robotics/match_start.mp3")
        print("load")
        mixer.music.play()
        print("play")
        sleep(2)
        mixer.music.stop()
        print("stop")
        
        print("Let's GO!!")
	
        self.myLED = StatusLED()
        ledBlink = threading.Thread(target=self.myLED.blink)
        ledBlink.daemon = True
        ledBlink.start()
        
        for event in self.controller.events():
            myEvent = self.controller.getEvent(event)
            self.action.process(myEvent)
            
            
        print("NEVER GONNA HAPPEN")
    @staticmethod        
    def cleanUp():
        #cleanup
        print("Need to clean up")
        mixer.music.load("ENDMATCH.mp3")
        mixer.music.play()
        sleep(2.5)
        mixer.music.stop()
        myLED = StatusLED()
        myLED.cleanUp()
        exit()
           
        
                        
if __name__ == '__main__':
    
    mybot = Main() 
    try:
        mybot.initialize()
    except KeyboardInterrupt:
        mybot.cleanUp()
