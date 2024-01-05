#!/usr/bin/python3


DEBUG = True
VIDEOTEST = True

# runs through a video tests for the PiCar-B

import RPi.GPIO as GPIO
import motor
import ultra
import socket
import time
import threading

import led
import os
from picamera2 import Picamera2, Preview
#from Picamera2.array import PiRGBArray
import cv2


import calValues


if __name__ == '__main__':

    camera = Picamera2()              #Camera initialization
    camera.configure(camera.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))
    camera.framerate = 7
 


    try:

        print ("-------------------")
        print ("-------------------")
        print (" PiCar2- Video Test")
        print (" Must be run from a GUI")
        print ("-------------------")
        print ("-------------------")
        print ()
        print ()

        if (VIDEOTEST):

            print ()
            print ("-------------------")
            print ("Open Video Window")
            print ("-------------------")


            camera.preview_configuration.main.size = (640,480)
            camera.preview_configuration.main.format = "RGB888"
            camera.preview_configuration.align()
            camera.configure("preview")
            camera.start()

            t_end = time.time() + 20 
            while time.time() < t_end:
                im= camera.capture_array()
                cv2.imshow("Video Test", im)
                if cv2.waitKey(1)==ord('q'):
                    break

            cv2.destroyAllWindows()
 

            camera.close()
    except KeyboardInterrupt:
        print("done") 
