import time
import grovepi

# Connect the Grove lightsensor to digital port D3
lightsensor = 3

grovepi.pinMode(lightsensor,"INPUT")

while True:
    try:
        print(grovepi.digitalRead(lightsensor))
        time.sleep(.5)

    except IOError:
        print ("Error")
