# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       david                                                        #
# 	Created:      9/13/2025, 7:23:17 PM                                        #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

brain = Brain()

def autonomous():
    brain.screen.clear_screen()
    brain.screen.print("autonomous code")
    # place automonous code here

def user_control():
    brain.screen.clear_screen()
    brain.screen.print("driver control")
    # place driver control in this while loop
    while True:
        rightX = controller.axis1.position()
        rightY = controller.axis2.position()
        leftX = controller.axis4.position()
        leftY = controller.axis3.position()
        print("\n\n\n\n\n\n\n\n\n\n")
        print(rightX)
        print(rightY)
        print(leftX)
        print(leftY)

        finalLeftMotorPow, finalRightMotorPow = leftY, leftY
        
        
        if leftY > 0:
            if rightX > 0:
                finalRightMotorPow -= 0.75 * rightX
            elif rightX < 0:
                finalLeftMotorPow += 0.75 * rightX
            leftMotor.spin(FORWARD, finalLeftMotorPow)
            rightMotor.spin(REVERSE, finalRightMotorPow)
        elif leftY < 0:
            if rightX > 0:
                finalRightMotorPow += 0.75 * rightX
            elif rightX < 0:
                finalLeftMotorPow -= 0.75 * rightX
            leftMotor.spin(FORWARD, finalLeftMotorPow)
            rightMotor.spin(REVERSE, finalRightMotorPow)
        else:
            leftMotor.stop()
            rightMotor.stop()
        


        

        wait(20, MSEC)

# create competition instance
comp = Competition(user_control, autonomous)

# actions to do when the program starts
brain.screen.clear_screen()
controller = Controller()

leftMotor = Motor(1)
rightMotor = Motor(2)
finalLeftMotorPow = 0
finalRightMotorPow = 0
print("a")