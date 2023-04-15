import cv2 as cv2
import os
import grovepi
import time

# Connect the Grove ultrasonic sensor to digital port D3
ultrasonicsensor = 3

grovepi.pinMode(ultrasonicsensor,"INPUT")

# Connect the Grove relay to digital port D5
relay = 5

grovepi.pinMode(relay,"OUTPUT")

print("Started")
# Load pre-trained face detection model
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Load pre-trained face recognition model
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('recognizer/trainer.yml')

# Set the name for the recognized user
user_name = 'Donald Trump'

# Initialize the camera
camera = cv2.VideoCapture(0)
print("in loop")

while True:
    if (grovepi.ultrasonicRead(ultrasonicsensor) < 100):
        # Capture the video stream from the camera
        ret, frame = camera.read()

        # Convert the video stream to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the grayscale video stream
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)

        # Iterate through the detected faces
        for (x, y, w, h) in faces:
            # Crop the face image from the video stream
            face = gray[y:y+h, x:x+w]

            # Resize the cropped face image to match the size of the training data
            face = cv2.resize(face, (150, 150))

            # Recognize the face using the pre-trained face recognition model
            label, confidence = recognizer.predict(face)

            # If the recognized user's ID matches the pre-defined user ID, unlock the door
            if confidence < 70:
                print('Welcome, ' + user_name + '!')
                grovepi.digitalWrite(relay,1)     # Send HIGH to switch on relay
                print ("Door open!")
                time.sleep(10)
            else:
                print('Unauthorized access!')
                grovepi.digitalWrite(relay,0)     # Send LOW to switch off relay
                print ("Door lock!")
        grovepi.digitalWrite(relay,0)     # Send LOW to switch off relay
        # Display the video stream with detected faces
        cv2.imshow('Face Recognition Door Lock System', frame)

        # Wait for the user to press the 'q' key to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release the camera and destroy all windows
camera.release()
cv2.destroyAllWindows()
