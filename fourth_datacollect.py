import paho.mqtt.subscribe as subscribe
import datetime


while True:
    file1 = open("sensor1.csv", 'ab')
    s1= subscribe.simple("test1/topic",hostname="192.168.151.154")
    s2= subscribe.simple("test2/topic",hostname="192.168.151.154")
    s3= subscribe.simple("test3/topic",hostname="192.168.151.154")
    s4= subscribe.simple("test4/topic",hostname="192.168.151.154")
    s5= subscribe.simple("test5/topic",hostname="192.168.151.154")
    s6= subscribe.simple("test6/topic",hostname="192.168.151.154")
    s7= subscribe.simple("test7/topic",hostname="192.168.151.154")
    s8= subscribe.simple("test8/topic",hostname="192.168.151.154")
    date1 =str(datetime.datetime.now())
    print(datetime.datetime.now()," 1)",s1.payload," ","2)",s2.payload)
    file1.write(s1.payload)
    file1.close()
    file1 = open("sensor1.csv", 'a')
    file1.write("\n")
    file1.close()




    file2 = open("sensor2.csv", 'ab')
    file2.write(s2.payload)
    file2.close()
    file2 = open("sensor2.csv", 'a')
    file2.write("\n")
    file2.close()


    file3 = open("sensor3.csv", 'ab')
    file3.write(s3.payload)
    file3.close()
    file3 = open("sensor3.csv", 'a')
    file3.write("\n")
    file3.close()



    file4 = open("sensor4.csv", 'ab')
    file4.write(s4.payload)
    file4.close()
    file4 = open("sensor4.csv", 'a')
    file4.write("\n")
    file4.close()



    file5 = open("sensor5.csv", 'ab')
    file5.write(s5.payload)
    file5.close()
    file5= open("sensor5.csv", 'a')
    file5.write("\n")
    file5.close()


    file6 = open("sensor6.csv", 'ab')
    file6.write(s6.payload)
    file6.close()
    file6 = open("sensor6.csv", 'a')
    file6.write("\n")
    file6.close()


    file7 = open("sensor7.csv", 'ab')
    file7.write(s7.payload)
    file7.close()
    file7 = open("sensor7.csv", 'a')
    file7.write("\n")
    file7.close()



    file8 = open("sensor8.csv", 'ab')
    file8.write(s8.payload)
    file8.close()
    file8 = open("sensor8.csv", 'a')
    file8.write("\n")
    file8.close()