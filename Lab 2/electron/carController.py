import wheelController

class carController:

    wheel_c = wheelController.wheelController()
    totalDistance = 0
    headingAngle = 0
    driveConstant = 1
    speed = 0


    def handleCommand(self, commandStr):
        sec = 2
        powLevel = 15

        # print(commandStr)
        cmdStr = commandStr.decode()
        # print(cmdStr)

        returnStr = "COMMAND_NOT_SUPPORTED"
        if(cmdStr == "87"):
            returnStr = "DRIVING_FORWARD"
            # print("HERE1")
            self.wheel_c.forward(sec, powLevel)
            # print("HERE2")
            self.totalDistance = self.totalDistance + self.driveConstant
            self.headingAngle = "FORWARD"
            self.speed = powLevel
        elif (cmdStr == "83"):
            returnStr = "DRIVING_BACKWARD"
            self.wheel_c.backward(sec, powLevel)
            self.totalDistance = self.totalDistance - self.driveConstant
            self.headingAngle = "BACKWARD"
            self.speed = powLevel
        elif (cmdStr == "68"):
            returnStr = "TURNING_RIGHT"
            self.wheel_c.turn_right(sec, powLevel)
            self.totalDistance = self.totalDistance + self.driveConstant
            self.headingAngle = "RIGHT"
            self.speed = powLevel
        elif (cmdStr == "65"):
            returnStr = "TURNING_LEFT"
            self.wheel_c.turn_left(sec, powLevel)
            self.totalDistance = self.totalDistance + self.driveConstant
            self.headingAngle = "LEFT"
            self.speed = powLevel
        elif (cmdStr == "INFO"):
            print("INFO")
            returnStr = self.getCarInfo()


        return returnStr



    def getCarInfo(self):
        infoStr = str(self.headingAngle) + "," + str(self.speed) + "," + str(self.totalDistance) + "," + str(self.wheel_c.PiTemp())
        return infoStr
            