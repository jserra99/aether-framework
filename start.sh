#!/bin/bash
echo "Please enter the new password to use to login to the pi, as a member of team 753 you should know what to put"
sudo passwd pi
git clone https://github.com/jserra99/aether-framework.git
sudo pip3 install adafruit-circuitpython-neopixel
