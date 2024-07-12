import paho.mqtt.subscribe as subscribe
import csv
import datetime
a=[]
while True:
     file = open("mpu_data.csv", 'a')
     msg1= subscribe.simple("test/topic",hostname="192.168.43.58")
     msg2= subscribe.simple("test21/topic",hostname="192.168.43.58")
     date =str(datetime.datetime.now())
     print(datetime.datetime.now()," 1)",msg1.payload," ","2)",msg2.payload)

     temp = "\n"+date+",1,"+str(msg1.payload)+",2,"+str(msg2.payload)
     file.write(temp)
     file.close()
