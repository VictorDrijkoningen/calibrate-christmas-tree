

#import cv2
import os
import json
import random

number_leds = 100
screen_dim = (10,10)
output_file="./calibration.json"

def test_take_picture(dev_num):
    with cv2.VideoCapture(dev_num) as cam:
        if not cam.isOpened():
            raise IOError
        ret, frame = cam.read()
        cv2.imshow("frame", frame)



def save_calibration(calibration: dict):
  with open(output_file, 'w') as fp:
    json.dump(calibration, fp)


def get_closest(pixel, calibration):
  #print( list(calibration.keys())[list(calibration.values()).index(pixel)] )
  #if calibration.index(pixel):
  #  pass

  out = 0
  dist = 99999
  for i in range(int(calibration["number_leds"])):
    nextdist = (pixel[0]-calibration[i][0])**2 + (pixel[1]-calibration[i][1])**2
    if nextdist < dist:
      dist = nextdist
      out = str(i)
  return out

def add_map(calibration):
  for x in range(screen_dim[0]):
    print(f"addmap {x}/{screen_dim[0]}")
    for y in range(screen_dim[1]):
      calibration[str( (x,y) )] = get_closest((x,y), calibration)

def make_rand_calibration():
  calibration = dict()
  calibration["number_leds"] = number_leds
  calibration["screen_dim"] = screen_dim
  for i in range(number_leds):
    calibration[i] = random.randint(0,screen_dim[0]), random.randint(0,screen_dim[1])
  
  add_map(calibration)
  return calibration

#print(make_rand_calibration())
save_calibration(make_rand_calibration())


