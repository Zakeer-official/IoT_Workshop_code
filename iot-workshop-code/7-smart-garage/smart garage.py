import time
import grovepi

# Connect the Grove ultrasonic sensor to digital port D3
ultrasonicsensor = 3
grovepi.pinMode(ultrasonicsensor,"INPUT")

# Connect the Grove relay to digital port D5
relay = 5
grovepi.pinMode(relay,"OUTPUT")
time.sleep(1)

def opengarage():
    grovepi.digitalWrite(relay,1)
    print ("Opening Garage...")
    
def closegarage():
    grovepi.digitalWrite(relay,0)
    print ("Closing Garage...")
        
while True:
    if (grovepi.ultrasonicRead(ultrasonicsensor) < 100):
        opengarage()
        time.sleep(60)
    else:
        closegarage()
    print("Distance: ",grovepi.ultrasonicRead(ultrasonicsensor),"cm")
    time.sleep(1)