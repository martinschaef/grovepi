# Clap-clap sensor for Hue lights with GrovePi #

## Setup ##
- Make sure you have the GrovePi installed properly. 
- Connect the sound sensor to analog port 0 of the grovepi and an LED to digital port 4.
- Make sure you have https://github.com/allanbunch/beautifulhue installed.
- Look at switch_lights.py and adjust the login info for your Hue Bridge.

## Run ##
sudo python clap.py

Then clap twice to switch the light on/off ... The first clap will switch the LED at port 4 on to tell you that the script is listening. The second clap has to follow withn 0.2 to 0.8 seconds and will toggle the Hue lighs. If the LED switches off before the second clap, you have been too slow.

Currently, the setup is a bit vulnerable to vibrations and may be triggered by someone walking by if you have crappy wooden floors like I do. If so, try to mount the sound sensor somewhere else. 
