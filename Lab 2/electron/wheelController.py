import picar_4wd as fc
import time


class wheelController:

    def forward(self, seconds, powerLevel):
        # This function will have picar move in the forward direction
        # for the requested amount of time and power level input by the user.
        try:
            fc.forward(powerLevel) 
            time.sleep(seconds)
        finally:
            fc.stop()

    def backward(self, seconds, powerLevel):
        try:
            fc.backward(powerLevel) 
            time.sleep(seconds)
        finally:
            fc.stop()


    def turn_left(self, seconds, powerLevel):
            try:
                fc.turn_left(powerLevel)
                time.sleep(seconds)
            finally:
                fc.stop()


    def turn_right(self, seconds, powerLevel):
        try:
            fc.turn_right(powerLevel)
            time.sleep(seconds)
        finally:
            fc.stop()


    def stop(self):
        fc.stop();



    def PiTemp(self):
        return fc.cpu_temperature()


if __name__ == "__main__":
    wheel_C = wheelController()
    try:
        wheel_C.forward(1, 10)
    finally:
        wheel_C.stop