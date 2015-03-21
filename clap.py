# This is a simple clap-clap sensor to turn hue lights on/off

# GrovePi + Grove Sound Sensor + Grove LED
# http://www.seeedstudio.com/wiki/Grove_-_Sound_Sensor
# http://www.seeedstudio.com/wiki/Grove_-_LED_Socket_Kit

import time
import grovepi
import switch_lights

# Connect the Grove Sound Sensor to analog port A0
# SIG,NC,VCC,GND
sound_sensor = 0

# Connect the Grove LED to digital port D5
# SIG,NC,VCC,GND
led = 4

grovepi.pinMode(sound_sensor, "INPUT")
grovepi.pinMode(led, "OUTPUT")

# set the interval for the second clap (in seconds)
min_interval = 0.3
max_interval = 0.9
# control variables
clap = 0
clap_time = time.time()

#switch the LED off initially
grovepi.digitalWrite(led, 0)

print("measure the background noise")
total_noise = 0
sample_size = 40.0
i = 0
while i < sample_size:
    try:
        sensor_value = grovepi.analogRead(sound_sensor)
        # print sensor_value
        total_noise += sensor_value
        i += 1
    except IOError:
        pass # ignore sensor hiccups
print float(total_noise) / sample_size

# now set the threshold to something bigger than the avg noise.
threshold_value = float(total_noise) / sample_size * 2.0
print("threshold ", threshold_value)

# main loop:
# listen to the sensor. If a clap is recorded, set the
# 'clap' variable to 1 and switch the LED on to tell the
# user that we are waiting for the second clap.
# if the second clap is not recorded in time, set 'clap'
# to zero again and switch the LED off.
# If the second clap is recorded, call 'switch_lights.switch_lights()'
# and sleep for 2 seconds to avoid chaos.
while True:
    try:
        # Read the sound level
        sensor_value = grovepi.analogRead(sound_sensor)

        # check if we already hear the first clap.
        if clap == 1:
            # if so, check if the second clap is overdue.
            if (time.time() - clap_time) > max_interval:
                # if so, reset clap to 0 and switch the
                # control light off
                clap = 0
                # Switch the LED off the signal the user
                # that we are not listening anymore.
                grovepi.digitalWrite(led, clap)

        # If loud, do something
        if sensor_value > threshold_value:
            if clap == 0:
                # If this was the first clap, set 'clap' to one,
                # get the current time, and switch the LED on to
                # tell the user that we are waiting for the second
                # clap.
                clap = 1
                clap_time = time.time()
                grovepi.digitalWrite(led, clap)
            else:
                # If clap is already one then this must be the second
                # clap.
                # Get the delta time since the last clap.
                dt = time.time() - clap_time
                if min_interval < dt < max_interval:
                    # If the delta time since the last clap is in the interval,
                    # we have found our second clap and can toggle the lights.
                    switch_lights.switch_lights()
                    # Now, set clap to zero and switch the LED off to reset everything
                    # and wait for the next clap-clap.
                    clap = 0
                    grovepi.digitalWrite(led, clap)
                    print "Double clap at ... ", time.time()
                    print "Sleeping for 2s... "
                    # Sleep for 2 seconds to avoid blinking lights if somebody plays
                    # the drums or something.
                    time.sleep(2.0)

    except IOError:
        pass
