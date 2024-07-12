import numpy as np
import csv
import matplotlib.pyplot as plt


arr1 = np.loadtxt("first_without_tremor.csv",delimiter=",", dtype=str)
arr2 = np.loadtxt("first_with_tremors.csv",delimiter=",", dtype=str)

timestan=arr1[:,0]
timestan=[x[11:19] for x in timestan]

AX1=arr1[:,1]
AX1=[float(i) for i in AX1]
AY1=arr1[:,2]
AY1=[float(i) for i in AY1]
AZ1=arr1[:,3]
AZ1=[float(i) for i in AZ1]
GX1=arr2[:,1]
GX1=[float(i) for i in GX1]
GY1=arr2[:,2]
GY1=[float(i) for i in GY1]
GZ1=arr2[:,3]
GZ1=[float(i) for i in GZ1]
AX2=arr1[:,7]
AX2=[float(i) for i in AX2]
AY2=arr1[:,8]
AY2=[float(i) for i in AY2]
AZ2=arr1[:,9]
AZ2=[float(i) for i in AZ2]
GX2=arr2[:,7]
GX2=[float(i) for i in GX2]
GY2=arr2[:,8]
GY2=[float(i) for i in GY2]
GZ2=arr2[:,9]
GZ2=[float(i) for i in GZ2]

fig ,axs = plt.subplots(2,2)

axs[0,0].plot(AX1)
axs[0,0].plot(AY1)
axs[0,0].plot(AZ1)
axs[0,0].set_title("Sensor 1 acceleration without tremor: ")

axs[0,1].plot(GX1)
axs[0,1].plot(GY1)
axs[0,1].plot(GZ1)
axs[0,1].set_title("Sensor 1 acceleration with tremor : ")

axs[1,0].plot(AX2)
axs[1,0].plot(AY2)
axs[1,0].plot(AZ2)
axs[1,0].set_title("Sensor 2 acceleration without tremor: ")

axs[1,1].plot(GX2)
axs[1,1].plot(GY2)
axs[1,1].plot(GZ2)
axs[1,1].set_title("Sensor 2 acceleration with tremor : ")

plt.show()








































