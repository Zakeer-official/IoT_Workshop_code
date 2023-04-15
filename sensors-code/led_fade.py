import time
import grovepi

# Connect the Grove LED to digital port D5
led = 5

grovepi.pinMode(led,"OUTPUT")
time.sleep(1)
i = 0

while True:
    try:
        # Reset
        if i > 255:
            i = 0

        # Current brightness
        print (i)

        # Give PWM output to LED
        grovepi.analogWrite(led,i)

        # Increment brightness for next iteration
        i = i + 5
        time.sleep(.1)

    except KeyboardInterrupt:
        grovepi.analogWrite(led,0)
        break
    except IOError:
        print ("Error")