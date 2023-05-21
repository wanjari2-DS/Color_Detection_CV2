#OBJECT DETECTION USING OPENCV 

'''How can we detect which color it is and how can way say to the computer only 1 specific color
that is what we are going to see using opencv'''

import cv2 
import numpy as np

cap = cv2.VideoCapture(0) 

while True:
    _, frame = cap.read() 
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cv2.imshow("Frame", frame) 
    
    key = cv2.waitKey(1)
    if key ==27:
        break

''' HSV --> HUE - we can see the color red,green,blue,yellow and also we can see the gradiation of the color         
          SATURATION - How much quantity of the color we want to have 
          (0- nothing, completely white, opencv - maximux pixel 0-255)
          VALUE - Brightness of the color (0- completely black)'''
#==============================================================================       



# Only Red color detection
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    low_red = np.array([161, 155, 84]) 
    high_red = np.array([179, 255, 255])        
    red_mask = cv2.inRange(hsv_frame, low_red, high_red) 
    red = cv2.bitwise_and(frame, frame, mask=red_mask)

    cv2.imshow("Frame", frame) 
    cv2.imshow('Red', red)
    
    key = cv2.waitKey(1)
    if key ==27:
        break

#=============================================================================


# Only Green Color 

import cv2
import numpy as np
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    low_green = np.array([25, 52, 72])
    high_green = np.array([102, 255, 255])
    green_mask = cv2.inRange(hsv_frame, low_green, high_green)
    green = cv2.bitwise_and(frame, frame, mask=green_mask)

    cv2.imshow("Frame", frame) 
    cv2.imshow('Green', green)
        
    key = cv2.waitKey(1)
    if key ==27:
        break

#=============================================================================

# Only Blue color Detection
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    low_blue = np.array([94, 80, 2])
    high_blue = np.array([126, 255, 255])
    blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
    blue = cv2.bitwise_and(frame, frame, mask=blue_mask)

    cv2.imshow("Frame", frame) 
    cv2.imshow('Blue', blue)
    
    
    key = cv2.waitKey(1)
    if key ==27:
        break
    
#============================================================================


# Every color except White 
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
  
    low = np.array([0, 42, 0]) 
    high = np.array([179, 255, 255])
    mask = cv2.inRange(hsv_frame, low, high)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("Frame", frame) 
    cv2.imshow('Result', result)
    
    
    key = cv2.waitKey(1)
    if key ==27:
        break
