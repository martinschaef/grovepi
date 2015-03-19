# Clap sensor for Hue lights with GrovePi #

## Setup ##
- Make sure you have the GrovePi installed properly. 
- Connect the sound sensor to analog port 0 of the grovepi and an LED to digital port 4.
- Make sure you have https://github.com/allanbunch/beautifulhue installed.
- Look at switch_lights.py and adjust the login info for your Hue Bridge.

## Run ##
sudo python clap.py

Then clap twice to switch the light on/off ...
