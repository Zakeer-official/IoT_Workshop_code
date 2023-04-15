import cv2 as cv2
import os
import grovepi
import time

# Connect the Grove ultrasonic sensor to digital port D3
ultrasonicsensor = 3
grovepi.pinMode(ultrasonicsensor,"INPUT")

# Connect the Grove button to digital port D3
button = 4
grovepi.pinMode(button,"INPUT")


# Connect the Grove buzzer to digital port D5
buzzer = 5
grovepi.pinMode(buzzer,"OUTPUT")

# Connect the Grove relay to digital port D6
relay = 6
grovepi.pinMode(relay,"OUTPUT")

# Initialize the camera
camera = cv2.VideoCapture(0)
print("in loop")

while True:
    if (grovepi.ultrasonicRead(ultrasonicsensor) < 10):
        grovepi.digitalWrite(buzzer,1)
        print("Someone at the door...")
        time.sleep(3)
        grovepi.digitalWrite(buzzer,0)
        
        ret, frame = camera.read()
        cv2.imshow('Door Bell System', frame)
        # Wait for the user to press the 'q' key to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        while grovepi.digitalRead(button) == False:
            grovepi.digitalWrite(relay,0)
        grovepi.digitalWrite(relay,1)
        time.sleep(5)
    else:
        grovepi.digitalWrite(buzzer,0)
        grovepi.digitalWrite(relay,0)
        cv2.destroyAllWindows()

# Release the camera and destroy all windows
camera.release()
cv2.destroyAllWindows()

