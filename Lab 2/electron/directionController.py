import picar_4wd as fc
import time


class directionController:

    def left(self, secs, powLevel):
         #This function is designed to instruct the picar to turn left for a specified
        # duration and with a power level determined by the user.
            try:
                fc.turn_left(powLevel)
                time.sleep(secs)
            finally:
                fc.stop()


    def right(self, secs, powLevel):
         #This function is designed to instruct the picar to turn right for a specified
        # duration and with a power level determined by the user.
        try:
            fc.turn_right(powLevel)
            time.sleep(secs)
        finally:
            fc.stop()

    def front(self, secs, powLevel):
        #This function is designed to instruct the picar to move forward for a specified
        # duration and with a power level determined by the user.
        try:
            fc.forward(powLevel) 
            time.sleep(secs)
        finally:
            fc.stop()

    def back(self, secs, powLevel):
         #This function is designed to instruct the picar to move backward for a specified
        # duration and with a power level determined by the user.
        try:
            fc.backward(powLevel) 
            time.sleep(secs)
        finally:
            fc.stop()

    def stop(self):
         #This function is designed to instruct the picar to stop.
        fc.stop();



    def getPiTemp(self): 
         #This function is designed to get the temperature stats from PI

        return fc.cpu_temperature()
    


    


if __name__ == "__main__":
    dir_c = directionController()
    try:
        dir_c.front(1, 10)
    finally:
        dir_c.stop