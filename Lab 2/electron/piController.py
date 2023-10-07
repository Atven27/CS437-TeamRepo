import directionController

class piController:

    pi_c = directionController.directionController() 
    distanceTravelled = 0  # total distance travelled by the car
    direction = 0  # direction in which the car is moving
    distance = 1   
    speed = 0


    def directionHandle(self, inputStr):
        sec = 2
        powLevel = 20

        inpStr = inputStr.decode() # decoding the input string received from the UI


        outputStr = "COMMAND_NOT_FOUND"
        if(inpStr == "87"):
            # Instruct car to move forward if the decoded input string is "87".
            # Calculate the speed, distance travelled and the direction of the car to send the info back to the UI.
            outputStr = "MOVING_FORWARD"
            self.pi_c.front(sec, powLevel)
            self.distanceTravelled = self.distanceTravelled + self.distance
            self.direction = "FORWARD"
            self.speed = powLevel
        elif (inpStr == "65"):
            # Instruct car to turn left if the decoded input string is "65".
            # Calculate the speed, distance travelled and the direction of the car to send the info back to the UI.
            outputStr = "TURN_LEFT"
            self.pi_c.left(sec, powLevel)
            self.distanceTravelled = self.distanceTravelled + self.distance
            self.direction = "LEFT"
            self.speed = powLevel
        elif (inpStr == "83"):
            # Instruct car to move backward if the decoded input string is "83".
            # Calculate the speed, distance travelled and the direction of the car to send the info back to the UI.
            outputStr = "MOVING_BACKWARD"
            self.pi_c.back(sec, powLevel)
            self.distanceTravelled = self.distanceTravelled - self.distance
            self.direction = "BACKWARD"
            self.speed = powLevel
        elif (inpStr == "68"):
            # Instruct car to turn right if the decoded input string is "68".
            # Calculate the speed, distance travelled and the direction of the car to send the info back to the UI.
            outputStr = "TURN_RIGHT"
            self.pi_c.right(sec, powLevel)
            self.distanceTravelled = self.distanceTravelled + self.distance
            self.direction = "RIGHT"
            self.speed = powLevel
        
        elif (inpStr == "INFO"):
            # Sending back the info collected from the PI.
            print("INFO")
            outputStr = self.getPiInfo()


        return outputStr



    def getPiInfo(self):
        # Info collected from the PI
        piInfoStr = str(self.direction) + "," + str(self.speed) + "," + str(self.distanceTravelled) + "," + str(self.pi_c.getPiTemp())
        return piInfoStr
            