

import cv2
import os



def take_picture(dev_num):
    with cv2.VideoCapture(dev_num) as cam:
        if not cam.isOpened():
            raise IOError
        
        ret, frame = cam.read()
        cv2.imshow("frame", frame)
