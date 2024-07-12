import numpy as np
import csv
import matplotlib.pyplot as plt


lt = np.loadtxt("second_left_without_tremor.csv",delimiter=",", dtype=str)
rt = np.loadtxt("second_right_without_tremor.csv",delimiter=",", dtype=str)
lwt = np.loadtxt("second_left_with_tremors.csv",delimiter=",", dtype=str)
rwt = np.loadtxt("second_right_with_tremors.csv",delimiter=",", dtype=str)


LX=lt[:,1]
LX=[float(i) for i in LX]
LY=lt[:,2]
LY=[float(i) for i in LY]
LZ=lt[:,3]
LZ=[float(i) for i in LZ]
RX=rt[:,1]
RX=[float(i) for i in RX]
RY=rt[:,2]
RY=[float(i) for i in RY]
RZ=rt[:,3]
RZ=[float(i) for i in RZ]



LXT=lwt[:,1]
LXT=[float(i) for i in LXT]
LYT=lwt[:,2]
LYT=[float(i) for i in LYT]
LZT=lwt[:,3]
LZT=[float(i) for i in LZT]
RXT=rwt[:,1]
RXT=[float(i) for i in RXT]
RYT=rwt[:,2]
RYT=[float(i) for i in RYT]
RZT=rwt[:,3]
RZT=[float(i) for i in RZT]

fig ,axs = plt.subplots(2,2)

axs[0,0].plot(LX)
axs[0,0].plot(LY)
axs[0,0].plot(LZ)
axs[0,0].set_title("Left Hand acceleration without tremor: ")

axs[0,1].plot(LXT)
axs[0,1].plot(LYT)
axs[0,1].plot(LZT)
axs[0,1].set_title("Left Hand acceleration with tremor : ")

axs[1,0].plot(RX)
axs[1,0].plot(RY)
axs[1,0].plot(RZ)
axs[1,0].set_title("Right Hand acceleration without tremor: ")

axs[1,1].plot(RXT)
axs[1,1].plot(RYT)
axs[1,1].plot(RZT)
axs[1,1].set_title("Right Hand acceleration with tremor : ")

plt.show()








































