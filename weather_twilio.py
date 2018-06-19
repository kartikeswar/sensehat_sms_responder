#!/usr/bin/python
from sense_hat import SenseHat
import time
import sys

sense = SenseHat()
sense.clear()

try:
      while True:
           file_object = open("../kko_twilio_app/temp.txt","w+")
           temp = sense.get_temperature()
           temp = round(temp, 1)
           print("Temperature C",temp) 
           temp_string = "Temp is {} C".format(temp)

           humidity = sense.get_humidity()  
           humidity = round(humidity, 1)  
           print("Humidity :",humidity) 
           hum_string = "Humidity is {}".format(humidity)

           pressure = sense.get_pressure()
           pressure = round(pressure, 1)
           print("Pressure:",pressure)
           pre_string = "Pressure is {}".format(pressure)
          
           comb_string = "%s %s %s"%(temp_string, hum_string, pre_string)
           file_object.write(comb_string)
           file_object.close()

           time.sleep(60)
except KeyboardInterrupt:
      pass

sense.clear()
