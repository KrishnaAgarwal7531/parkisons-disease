import paho.mqtt.subscribe as subscribe
import csv
import datetime
import matplotlib.pyplot as plt
a=[]
while True:
     msg1= subscribe.simple("test/topic",hostname="192.168.43.58")
     msg2= subscribe.simple("test21/topic",hostname="192.168.43.58")
     date =str(datetime.datetime.now())
     temp = str(msg1.payload)+str(msg2.payload)
     t=temp.split(',')
     #plt.plot(float(t[1]))
     #plt.show()
     print(float(t[1]))