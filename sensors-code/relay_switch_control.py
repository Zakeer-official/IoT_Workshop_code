import time
import grovepi

# Connect the Grove Switch to digital port D3
switch = 3

# Connect the Grove Relay to digital port D5
relay = 5

grovepi.pinMode(switch,"INPUT")
grovepi.pinMode(relay,"OUTPUT")

while True:
    try:
        if grovepi.digitalRead(switch):
            grovepi.digitalWrite(relay,1)
        else:
            grovepi.digitalWrite(relay,0)

        time.sleep(.5)

    except KeyboardInterrupt:
        grovepi.digitalWrite(relay,0)
        break
    except IOError:
        print ("Error")
