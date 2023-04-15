import time
import grovepi

# Connect the Grove soundsensor to analog port A0
soundsensor = 14     # Pin 14 is A0 Port

grovepi.pinMode(soundsensor,"INPUT")
while True:
    try:
        sensor_value = grovepi.analogRead(soundsensor)
        print ("sensor_value = %d" %sensor_value)
        time.sleep(.5)

    except IOError:
        print ("Error")