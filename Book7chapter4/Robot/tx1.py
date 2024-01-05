import cv2
import numpy as np

cap = cv2.VideoCapture('/dev/video0', cv2.CAP_V4L)

#set dimensions
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 2560)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1440)

while cap.isOpened():
    ret, frame = cap.read()
    cv2.imwrite('Atharva_Naik.jpg' , frame)
    cv2.imshow('Video', frame)
    cv2.waitKey(0)
       
cap.release()
cv2.destroyAllWindows()  
