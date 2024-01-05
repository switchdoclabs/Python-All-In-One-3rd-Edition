#!/usr/bin/python3
# Robot Interface Test

import RobotInterface 
import time

RI = RobotInterface.RobotInterface()

print ("turn all off and center")

RI.centerAllServos()
RI.allLEDSOff()

import time

import Adafruit_PCA9685

import calValues

#import the settings for servos


pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)


#servo mapping
# pmw 0 head tilt
HEAD_TILT_SERVO = 0
# pwm 1 head turn
HEAD_TURN_SERVO = 1
# pwm 2 wheels turn
WHEELS_TURN_SERVO = 2


pwm.set_pwm(WHEELS_TURN_SERVO,0, 0)

pwm.set_pwm(HEAD_TURN_SERVO,0, 0)
pwm.set_pwm(HEAD_TILT_SERVO,0, 0)
