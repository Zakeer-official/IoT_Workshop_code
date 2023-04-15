import time
import math
import grovepi
import urllib.request
import requests
import threading
import json

# Set up the Grove sensors for the temperature sensor and door sensor
temp_humidity_sensor = 4     #Temperature sensor Port Number
therm_version = 0  # blue version
door_sensor = 3
grovepi.pinMode(door_sensor,"INPUT")
print("1")
# Set the threshold for the temperature
TEMPERATURE_THRESHOLD = 20

def thingspeak_post():
    threading.Timer(15,thingspeak_post).start()
    temp=round(get_temperature(),2)
    door_status = grovepi.digitalRead(door_sensor)
    URL =  "https://api.thingspeak.com/update?api_key=MT79B7HM6HZWZNKE"
    #HEADER  = "&field1={}&field2={}".format(temp,door_status)
    HEADER  = "&field1={}".format(temp)
    NEW_URL = URL + HEADER
    print("4")
    print(NEW_URL)
    data = urllib.request.urlopen(NEW_URL)
    print(data)

# Function to get the temperature from the sensor
def get_temperature():
    [temp,humidity] = grovepi.dht(temp_humidity_sensor,therm_version)
    print("3")
    return temp

# Function to regulate the temperature of the refrigerator
def regulate_temperature():
    temperature = get_temperature()
    print("2")
    if temperature > TEMPERATURE_THRESHOLD:
        # Code to decrease the temperature goes here
        print("Decreasing temperature...")
    elif temperature < TEMPERATURE_THRESHOLD:
        # Code to increase the temperature goes here
        print(" Increasing temperature...")

# Main loop to continuously regulate the temperature and check the door status
while True:
    regulate_temperature()
    thingspeak_post()
    time.sleep(1)
