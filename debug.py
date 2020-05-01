class Debug:
    @staticmethod
    def message(message, state):
        if(state==True) :
            print(message)
    @staticmethod
    def setDebug(state):
        if state == True:
            return True
        else:
            return False