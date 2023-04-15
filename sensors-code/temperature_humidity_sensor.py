import time
import math
import grovepi

temp_humidity_sensor    = 4     #Temperature sensor Port Number
therm_version = 0  # blue version

while True:
    try:
        [temp,humidity] = grovepi.dht(temp_humidity_sensor,therm_version)  
        if math.isnan(temp) == False and math.isnan(humidity) == False:
            print("temp = %.02f C humidity =%.02f \n"%(temp, humidity))
        time.sleep(5)
    except IOError:
        print ("Error")
        
