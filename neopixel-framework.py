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
connected = False
def connectionListener(connected, info):
    print(info, '; Connected=%s' % connected)
    with cond:
        notified[0] = True
        connected = True
        pixels.fill((0, 0, 0, 0))
        pixels.show()
        cond.notify()

NetworkTables.initialize(server='10.7.53.2') # roborio-753-frc.local
NetworkTables.addConnectionListener(connectionListener, immediateNotify=True)

with cond:
    print('Waiting')
    pixels.fill((255, 0, 0, 0))
    pixels.show()
    if not notified[0]:
        cond.wait()

# Our main code goes here

def main():
    table = NetworkTables.getTable('SmartDashboard')
    limelight = table.getAutoUpdateValue('limelight', False) # First parameter is the name of the instance, the second is the default value if nothing is found.
    robotEnabled = table.getAutoUpdateValue('robotEnabledPlaceholder', False)
    startTime = time.perf_counter()
    while True:
        timeElapsed = time.perf_counter() - startTime
        pixels.brightness = 0.05
        if robotEnabled:
            if limelight:
                pixels.brightness = 1.0
                pixels.fill((0, 255, 0, 0))
            else:
                pixels.fill((0, 0, 0, 0))
        else:
            if (timeElapsed % 2) >= 1:
                pixels.fill((0, 0, 255, 0))
            else:
                pixels.fill((0, 0, 0, 0))
        pixels.show()
        time.sleep(0.02)

if __name__ == '__main__':
    try:
        main()
    except:
        print("exception: exiting program")
        pixels.fill((0, 0, 0, 0))
        GPIO.cleanup()
