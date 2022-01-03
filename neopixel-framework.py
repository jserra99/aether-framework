# Docs: https://robotpy.readthedocs.io/en/stable/guide/nt.html#client-initialization-driver-station-coprocessor
import threading
from networktables import NetworkTables
import time
import board
import neopixel
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
num_pixels = 3
ORDER = neopixel.RGBW
pixel_pin = board.D18 # Neo pixel digital out connected to the 6th pin down on the second column
brightness_ = 1.0
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

NetworkTables.initialize(server='10.7.53.2') # roborio-753-frc.local
NetworkTables.addConnectionListener(connectionListener, immediateNotify=True)

with cond:
    print('Waiting')
    if not notified[0]:
        cond.wait()

# Our main code goes here
table = NetworkTables.getTable('SmartDashboard')
limelight = table.getAutoUpdateValue('limelight', False) # First parameter is the name of the instance, the second is the default value if nothing is found.
'''while True:
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
    time.sleep(0.01) # try to find a better method, maybe something asyncronous?'''
    

    
'''
NOTE: Start of psuedocode
loop forever:
    if the robot is disabled:
        make the pixels blink blue on and off every second but in between blinks check if the robot is enabled 

    else if the robot is enabled:
        if the rio is sending the signal to shine green:
            fill the pixels
            show the pixels
        otherwise:
            completely turn the pixels off
'''
