#!/bin/bash
echo "Please enter the new password to use to login to the pi, as a member of team 753 you should know what to put"
sudo passwd pi
sudo apt-get update
sudo apt-get upgrade
git clone https://github.com/jserra99/aether-framework.git
wget https://www.python.org/ftp/python/3.9.9/Python-3.9.9.tgz
tar -zxvf Python-3.9.9.tgz
cd Python-3.9.9
./configure --enable-optimizations
sudo make altinstall
cd /usr/bin
sudo rm python
sudo ln -s /usr/local/bin/python3.9 python
sudo pip3 install adafruit-circuitpython-neopixel
