import time
import grovepi

# Connect the Grove rotary angle sensor to analog port A0
rotaryanglesensor = 14     # Pin 14 is A0 Port.

grovepi.pinMode(rotaryanglesensor,"INPUT")

# Connect the Grove LED to digital port D5
led = 5

grovepi.pinMode(led,"OUTPUT")

while True:
    try:
        sensor_value = grovepi.analogRead(rotaryanglesensor)
        print ("sensor_value = %d" %sensor_value)
        # Give rotary angle sensor output to LED
        grovepi.analogWrite(led,int(sensor_value/4))
        time.sleep(.1)

    except KeyboardInterrupt:
        grovepi.analogWrite(led,0)
        break
    except IOError:
        print ("Error")