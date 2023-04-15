import time
import grovepi

# Connect the Grove ultrasonic sensor to digital port D3
ultrasonicsensor = 3

grovepi.pinMode(ultrasonicsensor,"INPUT")

# Connect the Grove LED to digital port D5
led = 5

grovepi.pinMode(led,"OUTPUT")
time.sleep(1)

while True:
    try:
        #LED control using ultrasonic sensor
        if (grovepi.ultrasonicRead(ultrasonicsensor) > 100):
            grovepi.digitalWrite(led,1)     # Send HIGH to switch on LED
            print ("LED ON!")
        else:
            grovepi.digitalWrite(led,0)     # Send LOW to switch off LED
            print ("LED OFF!")
        print("Distance: ",grovepi.ultrasonicRead(ultrasonicsensor),"cm")
        time.sleep(1)

    except KeyboardInterrupt:   # Turn LED off before stopping
        grovepi.digitalWrite(led,0)
        break
    except IOError:             # Print "Error" if communication error encountered
        print ("Error")
