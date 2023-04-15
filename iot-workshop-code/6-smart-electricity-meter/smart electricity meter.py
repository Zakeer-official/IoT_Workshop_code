import time
import math
import grovepi
import urllib.request
import requests
import threading
import json

# Connect the Grove Button to digital port D3
button = 3
grovepi.pinMode(button,"INPUT")

def thingspeak_post(energy):
    threading.Timer(15,thingspeak_post).start()
    URL =  "https://api.thingspeak.com/update?api_key=ZKBFV2VIVUI9B8LP"
    #HEADER  = "&field1={}&field2={}".format(temp,door_status)
    HEADER  = "&field1={}".format(energy)
    NEW_URL = URL + HEADER
    print(NEW_URL)
    data = urllib.request.urlopen(NEW_URL)
    print(data)

# Set up function to read energy consumption
def read_energy():
    # Measure energy consumption for 5 second
    start_time = time.time()
    energy = 0
    while time.time() < start_time + 5:
        if grovepi.digitalRead(button) == True:
            energy += 1
    return energy

# Main loop to continuously regulate the temperature and check the door status
while True:
    energy = read_energy()
    thingspeak_post(energy)
    time.sleep(1)

