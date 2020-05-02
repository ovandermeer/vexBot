from debug import Debug

class Action:
    def __init__(self,robot,debug, Main):
        self.debug = Debug.setDebug(debug)
        self.main = Main
            
        Debug.message("setting up actions",self.debug)
        self.robot = robot
        
    def process(self,action):
        if(action == "up"):
            self.robot.forward()
            Debug.message("Driving Forwards",self.debug)
        elif(action == "down"):
            self.robot.backward()
            Debug.message("Driving Backwards",self.debug)
        elif(action == "right"):
            self.robot.right()
            Debug.message("Turning Right",self.debug)
        elif(action == "left"):
            self.robot.left()
            Debug.message("Turning Left",self.debug)
        elif(action == "vertical dPad released"):
            self.robot.stop()
            Debug.message("Stopping",self.debug)
        elif(action == "horizontal dPad released"):
            self.robot.stop()
            Debug.message("Stopping",self.debug)
        elif(action == "xbox"):
            self.main.cleanUp()
            Debug.message("Stopping",self.debug)
        elif(action == "left bumper"):
            self.robot.extend()
            Debug.message("extend",self.debug)
        elif(action == "right bumper"):
            self.robot.retract()
            Debug.message("retract",self.debug)
        elif(action == "right bumper released" or action == "left bumper released"):
            self.robot.liftStop()
            Debug.message("lift stop",self.debug)
