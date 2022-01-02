# Docs: https://robotpy.readthedocs.io/en/stable/guide/nt.html#client-initialization-driver-station-coprocessor
import threading
#from networktables import NetworkTables
from time import sleep
import board
import neopixel
import RPi.GPIO as GPIO
import os
import sys

GPIO.setmode(GPIO.BCM)
num_pixels = 3
ORDER = neopixel.RGBW
pixel_pin = board.D18 # Neo pixel digital out connected to the 6th pin down on the second column
brightness_ = 0.01
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=brightness_, auto_write=False, pixel_order=ORDER)

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)

def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        sleep(wait)

def testRGB():
    while True:
        pixels.fill((255, 0, 0, 0))
        pixels.show()
        print('red')
        sleep(1)
        
        pixels.fill((0, 255, 0, 0))
        pixels.show()
        print('green')
        sleep(1)
        
        pixels.fill((0, 0, 255, 0))
        pixels.show()
        print('blue')
        sleep(1)
        
        pixels.fill((0, 0, 0, 0))
        pixels.show()
        print('off')
        sleep(1)

def main():
    while True:
        rainbow_cycle(0.001)
        # testRGB()
    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        try:
            pixels.fill((0, 0, 0, 0))
            pixels.show()
            sys.exit(0)
        except SystemExit:
            pixels.fill((0, 0, 0, 0))
            pixels.show()
            os._exit(0)
