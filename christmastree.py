
import board
import neopixel
import time
import json

pixels = neopixel.NeoPixel(board.D18, 100, auto_write=True)


def import_calibration(inputfile):
  with open(inputfile) as calibration:
    cali = json.load(calibration)
  return cali

def set_brightness(neopixels, brightness):
  neopixels.brightness = brightness

def screen_off(pixels, color=(0,0,0)):
  pixels.fill(color)
  pixels.show()


def set_screen(neopixels, pixel, color):
  neopixels[int(calibration[str(pixel)])] = color
  neopixels.show()

def test_pixels(neopixels):
  neopixels.fill((255,0,0))
  neopixels.show()
  time.sleep(0.5)
  neopixels.fill((0,255,0))
  neopixels.show()
  time.sleep(0.5)
  neopixels.fill((0,0,255))
  neopixels.show()
  time.sleep(0.5)
  neopixels.fill((0,0,0))
  neopixels.show()
  time.sleep(0.5)

calibration = import_calibration("calibration.json")

#print(calibration)

neopixels = neopixel.NeoPixel(board.D18, 100, auto_write=False)
set_brightness(neopixels, 127)
test_pixels(neopixels)



#time.sleep(5)
screen_off(neopixels)
