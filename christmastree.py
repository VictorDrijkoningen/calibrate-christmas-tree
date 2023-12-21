
import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.D18, 100, auto_write=True)


def set_brightness(brightness):
  pixels.brightness = brightness


def test(pixels):
  for i in range(len(pixels)):
    time.sleep(0.5)
    pixels[i] = (255, 0, 0)


def set_color(pixels, color):
  pixels.fill(color)


set_brightness(255)


set_color(pixels, (255,0,0))

set_color(pixels, (0,0,0))

test(pixels)
