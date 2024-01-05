#!/usr/bin/python3

# Stop all robot functions 
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

import RPi.GPIO as GPIO
import time
# motor_EN_A: Pin7  |  motor_EN_B: Pin11
# motor_A:  Pin8,Pin10    |  motor_B: Pin13,Pin12

Motor_A_EN    = 7
Motor_B_EN    = 11

Motor_A_Pin1  = 8
Motor_A_Pin2  = 10
Motor_B_Pin1  = 13
Motor_B_Pin2  = 12

Dir_forward   = 0
Dir_backward  = 1

pwm_A = 0
pwm_B = 0

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(Motor_A_EN, GPIO.OUT)
GPIO.setup(Motor_B_EN, GPIO.OUT)
GPIO.setup(Motor_A_Pin1, GPIO.OUT)
GPIO.setup(Motor_A_Pin2, GPIO.OUT)
GPIO.setup(Motor_B_Pin1, GPIO.OUT)
GPIO.setup(Motor_B_Pin2, GPIO.OUT)

GPIO.output(Motor_A_Pin1, GPIO.LOW)
GPIO.output(Motor_A_Pin2, GPIO.LOW)
GPIO.output(Motor_B_Pin1, GPIO.LOW)
GPIO.output(Motor_B_Pin2, GPIO.LOW)
GPIO.output(Motor_A_EN, GPIO.LOW)
GPIO.output(Motor_B_EN, GPIO.LOW)

GPIO.cleanup()             # Release resource


