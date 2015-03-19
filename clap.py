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

grovepi.pinMode(sound_sensor,"INPUT")
grovepi.pinMode(led,"OUTPUT")

# The threshold to turn the led on 400.00 * 5 / 1024 = 1.95v
threshold_value = 180
light=0
clap = 0
clap_time = 0.0

while True:
    try:
        # Read the sound level
        sensor_value = grovepi.analogRead(sound_sensor)

	if clap==1 and time.time()-clap_time>1.0:
             clap = 0
             grovepi.digitalWrite(led,0)

        # If loud, illuminate LED, otherwise dim
        if sensor_value > threshold_value:
             if clap == 0:
                 print("first")
                 grovepi.digitalWrite(led,light)
                 clap = 1
                 clap_time = time.time()
             else:	
                 dt =  time.time()-clap_time
                 print dt
                 if dt > 0.2 and dt < 0.5:
                     print("YEAAAAAH")
                     switch_lights.switch_lights()
                     grovepi.digitalWrite(led,0)
		 clap = 0 
             #print "sensor_value =", sensor_value
        #else:
        #    grovepi.digitalWrite(led,0)

        #print "sensor_value =", sensor_value
        #time.sleep(.02)

    except IOError:
        #print "Error"
        pass