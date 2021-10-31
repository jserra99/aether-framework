# vision-framework

A one-stop shop for your vision system.

# Getting Started:

If you are completely done assembling your aether-vision then you are now in the right place.
Start by downloading this repo as a zip and extract it somewhere where you won't lose it.
The first step is to flash a raspberry pi disc image onto a micro-sd card.
To do this we will be using a program called "rufus" linked here: https://rufus.ie/en/
Put the SD card into your computer and launch rufus.
Click into "device" and select the micro sd you previously inserted.
Then make sure the boot selection says "Disk or ISO image", then press select and navigate to the "INSERT_DISC_IMG_NAME" in the aether folder.
The rest of the rufus stuff will be documented later.
Finally, insert the micro-sd card into the raspberry pi and close up the enclosure.

# Setting up the pi

Now power your pi by either powering on the robot or powering the pi by other means and ssh into it via your preferred method whether that be wireless or wired.
For ease of use, we will be using remote desktop instead of putty when setting up, in the pit we may not have this luxury.
Launch "Remote Desktop", an application that should be pre-installed on you windows 10 computer.
For the computer simply put: "10.7.53.X"
Now that you are in launch the terminal in the top left corner, all of the necessary programs should already be on the pi but may need to be updated.
Simply type in "sh hello-world.sh" and hit enter, say 'Y' to any prompts that may pop up.
Now chameleon vision should be fully updated and installed on the pi.
To verify this type in "sudo java -jar chameleon-vision.jar" and hit enter, if everything goes correctly it should detect the pi-camera and launch a server at the address: "localhost:5800" on the pi or "10.7.53.X:5800" from the host pc.
If it is not working do not feel bad it is probably not your fault.
A guide on how to use and setup chameleon vision will be procured at a later time.

# Continuation

In this section we will go over the framework code for lighting up the neopixels.
Please open up neopixel-framework.py in your preferred code editior.
