# Docs: https://robotpy.readthedocs.io/en/stable/guide/nt.html#client-initialization-driver-station-coprocessor
import threading
from networktables import NetworkTables
from time import sleep
import board
import neopixel
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
num_pixels = 4 # change this value depending on the amount of neo pixels being used, this will be standardized in aether later on
pixels = neopixel.NeoPixel(board.D18,num_pixels) # make sure the data line of the neopixel/IC chip is connected to digital pin 18
presets = {
    'off': pixels.fill((0,0,0)),
    'green': pixels.fill((0,255,0)),
    'red': pixels.fill((255,0,0)),
    'blue': pixels.fill((0,0,255))
}

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
        presets['green']
        debug('green')
    else:
        # make sure neopixel is off
        presets['off']
        debug('off')
    sleep(0.01)
