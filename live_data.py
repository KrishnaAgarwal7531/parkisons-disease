import paho.mqtt.subscribe as subscribe
import datetime


while True:
    file = open("live.csv", 'ab')
    msg1= subscribe.simple("test4/topic",hostname="192.168.43.58")
    date1 =str(datetime.datetime.now())
    print(datetime.datetime.now()," 1)",msg1.payload)
    date1 =str(datetime.datetime.now())
    date = bytes(date1, 'utf-8')
    date = date1.encode('utf-8')
    temp = msg1.payload
    file.write(date)
    file.write(temp)
    file.close()
    file = open("live.csv", 'a')
    file.write("\n")
    file.close()