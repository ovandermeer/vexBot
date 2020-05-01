from debug import Debug
from evdev import InputDevice, categorize, ecodes

class GamePad():
    def __init__(self,debug):
        self.debug = Debug.setDebug(debug) 
        
        Debug.message("setting up gamePad",self.debug)
        self.device = InputDevice('/dev/input/event0')

        #button code variables (change to suit your device)
        self.aBtn = 304
        self.bBtn = 305
        self.xBtn = 307
        self.yBtn = 308

        self.up = 46
        self.down = 32
        self.left = 18
        self.right = 33

        self.start = 315
        self.select = 314
        
        self.xbox = 316

        self.lBump = 310
        self.rBump = 311

        self.lstick = 317
        self.rstick = 318

        self.dpadHorizontal = 16
        self.dpadVertical = 17
    
    def events(self):
        return self.device.read_loop()
        
    def getEvent(self,myEvent):
        returnString = "error"
        if myEvent.type == ecodes.EV_KEY:
            if myEvent.value == 1:
                if myEvent.code == self.yBtn:
                    returnString = "Y"
                elif myEvent.code == self.bBtn:
                    returnString = "B"
                elif myEvent.code == self.aBtn:
                    returnString = "A"
                elif myEvent.code == self.xBtn:
                    returnString = "X"

                elif myEvent.code == self.up:
                    returnString = "up"
                elif myEvent.code == self.down:
                    returnString = "down"
                elif myEvent.code == self.left:
                    returnString = "left"
                elif myEvent.code == self.right:
                    returnString = "right"

                elif myEvent.code == self.start:
                    returnString = "start"
                elif myEvent.code == self.select:
                    returnString = "select"
                    
                elif myEvent.code == self.xbox:
                    returnString = "xbox"

                elif myEvent.code == self.lBump:
                    returnString = "left bumper"
                elif myEvent.code == self.rBump:
                    returnString = "right bumper"

                elif myEvent.code == self.lstick:
                    returnString = "left stick"
                elif myEvent.code == self.rstick:
                    returnString = "right stick"
                    
            elif myEvent.value == 0:
                if myEvent.code == self.yBtn:
                    returnString = "Y released"
                elif myEvent.code == self.bBtn:
                    returnString = "B released"
                elif myEvent.code == self.aBtn:
                    returnString = "A released"
                elif myEvent.code == self.xBtn:
                    returnString = "X released"

                elif myEvent.code == self.up:
                    returnString = "up released"
                elif myEvent.code == self.down:
                    returnString = "down released"
                elif myEvent.code == self.left:
                    returnString = "left released"
                elif myEvent.code == self.right:
                    returnString = "right released"

                elif myEvent.code == self.start:
                    returnString = "start released"
                elif myEvent.code == self.select:
                    returnString = "select released"
                    
                elif myEvent.code == self.xbox:
                    returnString = "xbox released"

                elif myEvent.code == self.lBump:
                    returnString = "left bumper released"
                elif myEvent.code == self.rBump:
                    returnString = "right bumper released"

                elif myEvent.code == self.lstick:
                    returnString = "left stick released"
                elif myEvent.code == self.rstick:
                    returnString = "right stick released"
        if myEvent.value == 1:
            if myEvent.code == self.dpadHorizontal:
                 returnString = "right"
            elif myEvent.code == self.dpadVertical:
                 returnString = "down"
        elif myEvent.value == -1:
            if myEvent.code == self.dpadHorizontal:
                 returnString = "left"
            elif myEvent.code == self.dpadVertical:
                 returnString = "up"
        elif myEvent.value == 0:
            if myEvent.code == self.dpadHorizontal:
                 returnString = "horizontal dPad released"
            elif myEvent.code == self.dpadVertical:
                 returnString = "vertical dPad released"
                 
        return returnString

        
        