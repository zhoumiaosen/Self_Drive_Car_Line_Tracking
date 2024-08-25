# Python program to save a 
# video using OpenCV
  
import cv2
import motor
import time
import RPi.GPIO as gpio
import numpy as np

motor.setup()
center = 320
cap =cv2.VideoCapture(0)    
while(True):
    ret, frame = cap.read()
    if ret == True: 
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        retval, dst = cv2.threshold(gray,0,255,cv2.THRESH_OTSU)
        #print(retval)
        print(dst)
        dst=cv2.dilate(dst,None, iterations=2)
        cv2.imshow('Frame', dst)
        
        color = dst[400]
        white_count = np.sum(color ==255)
        white_index = np.where(color == 255)
        
        if white_count == 0:
            white_count = 1
        
        center = (white_index[0][white_count-1] + white_index[0][0])/2
        direction = center - 466
        print (direction)
        if abs(direction) > 250:
            motor.motorStop()
        #Left
        elif direction >= 0:
            if direction > 70:
                direction = 70
            motor.motor_A(-1, 30 + direction)
            motor.motor_B(1, 30 )
        
        #Right
        elif direction < 0:
            if direction < -70:
                direction = -70
            motor.motor_A(-1, 30)
            motor.motor_B(1, 30  - direction)
        # Press S on keyboard 
        # to stop the process
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
  
    # Break the loop
    else:
        break
  
# When everything done, release 
# the video capture and video 
# write objects
motor.motorStop()
cap.release()
# Closes all the frames
cv2.destroyAllWindows()
print("Ended")