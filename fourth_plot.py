import numpy as np
import csv
import matplotlib.pyplot as plt

rf = np.loadtxt("sensor1.csv",delimiter=",", dtype=str)
lf = np.loadtxt("sensor2.csv",delimiter=",", dtype=str)
lb = np.loadtxt("sensor3.csv",delimiter=",", dtype=str)
lt = np.loadtxt("sensor4.csv",delimiter=",", dtype=str)

rc = np.loadtxt("sensor5.csv",delimiter=",", dtype=str)
lc = np.loadtxt("sensor6.csv",delimiter=",", dtype=str)
rb = np.loadtxt("sensor7.csv",delimiter=",", dtype=str)
rt = np.loadtxt("sensor8.csv",delimiter=",", dtype=str)

print(lf)

#Array conversion for right forearm
rfE = rf[:,0]
rfE=[float(i) for i in rfE]
rfAX = rf[:,1]
rfAX=[float(i) for i in rfAX]
rfAY = rf[:,2]
rfAY=[float(i) for i in rfAY]
rfAZ = rf[:,3]
rfAZ=[float(i) for i in rfAZ]


#Array conversion for left forearm
lfE = lf[:,0]
lfE=[float(i) for i in lfE]
lfAX = lf[:,1]
lfAX=[float(i) for i in lfAX]
lfAY = lf[:,2]
lfAY=[float(i) for i in lfAY]
lfAZ = lf[:,3]
lfAZ=[float(i) for i in lfAZ]



#Array conversion for left bicep
lbE = lb[:,0]
lbE=[float(i) for i in lbE]
lbAX = lb[:,1]
lbAX=[float(i) for i in lbAX]
lbAY = lb[:,2]
lbAY=[float(i) for i in lbAY]
lbAZ = lb[:,3]
lbAZ=[float(i) for i in lbAZ]


#Array conversion for left thigh
ltE = lt[:,0]
ltE=[float(i) for i in ltE]
ltAX = lt[:,1]
ltAX=[float(i) for i in ltAX]
ltAY = lt[:,2]
ltAY=[float(i) for i in ltAY]
ltAZ = lt[:,3]
ltAZ=[float(i) for i in ltAZ]



#Array conversion for right calf
rcAX = rc[:,1]
rcAX=[float(i) for i in rcAX]
rcAY = rc[:,2]
rcAY=[float(i) for i in rcAY]
rcAZ = rc[:,3]
rcAZ=[float(i) for i in rcAZ]




#Array conversion for left calf
lcAX = lc[:,1]
lcAX=[float(i) for i in lcAX]
lcAY = lc[:,2]
lcAY=[float(i) for i in lcAY]
lcAZ = lc[:,3]
lcAZ=[float(i) for i in lcAZ]



#Array conversion for right bicep
rbAX = rb[:,1]
rbAX=[float(i) for i in rbAX]
rbAY = rb[:,2]
rbAY=[float(i) for i in rbAY]
rbAZ = rb[:,3]
rbAZ=[float(i) for i in rbAZ]


#Array conversion for right thigh
rtAX = rt[:,1]
rtAX=[float(i) for i in rtAX]
rtAY = rt[:,2]
rtAY=[float(i) for i in rtAY]
rtAZ = rt[:,3]
rtAZ=[float(i) for i in rtAZ]



fig ,axs = plt.subplots(2,4)

axs[0,0].plot(rfE)
axs[0,0].plot(rfAX)
axs[0,0].plot(rfAY)
axs[0,0].plot(rfAZ)
axs[0,0].set_xlim([100,200])
axs[0,0].set_title("Right Forearm acceleration and EMG on right hand : ")

axs[0,1].plot(lfE)
axs[0,1].plot(lfAX)
axs[0,1].plot(lfAY)
axs[0,1].plot(lfAZ)
axs[0,1].set_xlim([100,200])
axs[0,1].set_title("Left Forearm acceleration and EMG on left hand : ")

axs[0,2].plot(lbE)
axs[0,2].plot(lbAX)
axs[0,2].plot(lbAY)
axs[0,2].plot(lbAZ)
axs[0,2].set_xlim([100,200])
axs[0,2].set_title("Left Bicep acceleration and EMG on spine : ")


axs[0,3].plot(ltE)
axs[0,3].plot(ltAX)
axs[0,3].plot(ltAY)
axs[0,3].plot(ltAZ)
axs[0,3].set_xlim([100,200])
axs[0,3].set_title("Left thigh acceleration and EMG on left thigh: ")








axs[1,0].plot(rcAX)
axs[1,0].plot(rcAY)
axs[1,0].plot(rcAZ)
axs[1,0].set_xlim([100,200])
axs[1,0].set_title("Right Calf acceleration : ")


axs[1,1].plot(lcAX)
axs[1,1].plot(lcAY)
axs[1,1].plot(lcAZ)
axs[1,1].set_xlim([100,200])
axs[1,1].set_title("Left Calf acceleration : ")


axs[1,2].plot(rbAX)
axs[1,2].plot(rbAY)
axs[1,2].plot(rbAZ)
axs[1,2].set_xlim([100,200])
axs[1,2].set_title("Right Bicep acceleration : ")



axs[1,3].plot(rtAX)
axs[1,3].plot(rtAY)
axs[1,3].plot(rtAZ)
axs[1,3].set_xlim([100,200])
axs[1,3].set_title("Right thigh acceleration : ")

plt.show()