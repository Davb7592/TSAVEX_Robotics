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
        brain.screen.clear_screen()
        brain.screen.print("Right X: ", rightX)
        brain.screen.print("Right Y: ", rightY)
        brain.screen.print("Left X: ", leftX)
        brain.screen.print("Left Y: ", leftY)

        finalLeftMotorPow, finalRightMotorPow = leftY, leftY
        
        
        if leftY > 0:
            if rightX > 0:
                finalRightMotorPow -= 1.25 * rightX
            elif rightX < 0:
                finalLeftMotorPow += 1.25 * rightX
            leftMotor1.spin(FORWARD, finalLeftMotorPow)
            leftMotor2.spin(FORWARD, finalLeftMotorPow)
            leftMotor3.spin(REVERSE, finalLeftMotorPow)
            rightMotor1.spin(REVERSE, finalRightMotorPow)
            rightMotor2.spin(REVERSE, finalRightMotorPow)
            rightMotor3.spin(FORWARD, finalRightMotorPow)
        elif leftY < 0:
            if rightX > 0:
                finalRightMotorPow += 1.25 * rightX
            elif rightX < 0:
                finalLeftMotorPow -= 1.25 * rightX
            leftMotor1.spin(FORWARD, finalLeftMotorPow)
            leftMotor2.spin(FORWARD, finalLeftMotorPow)
            leftMotor3.spin(REVERSE, finalLeftMotorPow)
            rightMotor1.spin(REVERSE, finalRightMotorPow)
            rightMotor2.spin(REVERSE, finalRightMotorPow)
            rightMotor3.spin(FORWARD, finalRightMotorPow)
        else:
            leftMotor1.stop()
            leftMotor2.stop()
            leftMotor3.stop()
            rightMotor1.stop()
            rightMotor2.stop()
            rightMotor3.stop()
        


        

        wait(20, MSEC)

# create competition instance
comp = Competition(user_control, autonomous)

# actions to do when the program starts
brain.screen.clear_screen()
controller = Controller()

leftMotor1 = Motor(0)
leftMotor2 = Motor(1)
leftMotor3 = Motor(2)
rightMotor1 = Motor(3)
rightMotor2 = Motor(4)
rightMotor3 = Motor(5)
intakeMotor = Motor(6)
upDownMotor = Motor(7)

finalLeftMotorPow = 0
finalRightMotorPow = 0
