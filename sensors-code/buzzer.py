import time
import grovepi

# Connect the Grove Button to digital port D3
button = 3

grovepi.pinMode(button,"INPUT")

# Connect the Grove Buzzer to digital port D5
buzzer = 5

grovepi.pinMode(buzzer,"OUTPUT")

while True:
    try:
        if(grovepi.digitalRead(button) == True):
            grovepi.digitalWrite(buzzer,1)
        else: 
            grovepi.digitalWrite(buzzer,0)

    except KeyboardInterrupt:
        grovepi.digitalWrite(buzzer,0)
        break
    except IOError:
        print ("Error")
