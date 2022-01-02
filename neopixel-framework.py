# Docs: https://robotpy.readthedocs.io/en/stable/guide/nt.html#client-initialization-driver-station-coprocessor
import threading
from networktables import NetworkTables
from time import sleep
import board
import neopixel
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
num_pixels = 3
ORDER = neopixel.RGBW
pixel_pin = board.D18 # Neo pixel digital out connected to the 6th pin down on the second column
brightness_ = 1
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=brightness_, auto_write=False, pixel_order=ORDER)

DEBUG = True # change this to False to get rid of processor-wasteful print statements

def debug(message):
    if DEBUG:
        print(message)

cond = threading.Condition()
notified = [False]

def connectionListener(connected, info):
    print(info, '; Connected=%s' % connected)
    with cond:
        notified[0] = True
        cond.notify()

NetworkTables.initialize(server='10.7.53.2')
NetworkTables.addConnectionListener(connectionListener, immediateNotify=True)

with cond:
    print('Waiting')
    if not notified[0]:
        cond.wait()

# Our main code goes here
table = NetworkTables.getTable('SmartDashboard')
limelight = table.getAutoUpdateValue('limelight', False) # First parameter is the name of the instance, the second is the default value if nothing is found.
while True:
    if limelight.value:
        # light up neopixel
        pixels.fill((0, 255, 0, 0))
        pixels.show()
        debug('green')
    else:
        # make sure neopixel is off
        pixels.fill((0, 0, 0, 0))
        pixels.show()
        debug('off')
    sleep(0.01) # try to find a better method, maybe something asyncronous?
