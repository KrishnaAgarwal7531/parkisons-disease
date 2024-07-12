import paho.mqtt.subscribe as subscribe
import datetime


while True:
    file = open("espn.csv", 'ab')
    msg1= subscribe.simple("test/topic",hostname="192.168.43.58")
    msg2= subscribe.simple("test21/topic",hostname="192.168.43.58")
    date1 =str(datetime.datetime.now())
    print(datetime.datetime.now()," 1)",msg1.payload," ","2)",msg2.payload)
    date = bytes(date1, 'utf-8')
    date = date1.encode('utf-8')
    file.write(date)
    temp1 = msg1.payload
    temp2 = msg2.payload
    file.write(temp1)
    file.write(temp2)
    file.close()
    file = open("espn.csv", 'a')
    file.write("\n")
    file.close()