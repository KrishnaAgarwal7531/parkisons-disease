import paho.mqtt.subscribe as subscribe
import datetime


while True:
    file = open("espn1.csv", 'ab')
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
    file.close()
    file = open("espn1.csv", 'a')
    file.write("\n")
    file.close()
    file1 = open("espn2.csv", 'ab')
    file1.write(date)
    file1.write(temp2)
    file1.close()
    file1 = open("espn2.csv", 'a')
    file1.write("\n")
    file1.close()