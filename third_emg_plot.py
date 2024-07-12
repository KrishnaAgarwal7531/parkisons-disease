import numpy as np
import csv
import matplotlib.pyplot as plt


bff = np.loadtxt("finger_flex_bicep.csv",delimiter=",", dtype=str)
fff = np.loadtxt("finger_flex_forearm.csv",delimiter=",", dtype=str)
bst = np.loadtxt("shouldert_bicep.csv",delimiter=",", dtype=str)
fst = np.loadtxt("shouldert_forearm.csv",delimiter=",", dtype=str)
b90 = np.loadtxt("90deg_bicep.csv",delimiter=",", dtype=str)
f90 = np.loadtxt("90deg_forearm.csv",delimiter=",", dtype=str)
bbot = np.loadtxt("bottle_bicep.csv",delimiter=",", dtype=str)
fbot = np.loadtxt("bottle_forearm.csv",delimiter=",", dtype=str)


BF=bff[:,1]
BF=[float(i) for i in BF]
FF=fff[:,1]
FF=[float(i) for i in FF]


BS=bst[:,1]
BS=[float(i) for i in BS]
FS=fst[:,1]
FS=[float(i) for i in FS]


B9=b90[:,1]
B9=[float(i) for i in B9]
F9=f90[:,1]
F9=[float(i) for i in F9]



BB=bbot[:,1]
BB=[float(i) for i in BB]
FB=fbot[:,1]
FB=[float(i) for i in FB]



fig ,axs = plt.subplots(2,2)

axs[0,0].plot(BF)
axs[0,0].plot(FF)
axs[0,0].set_title("Finger Flex : ")

axs[0,1].plot(BS)
axs[0,1].plot(FS)
axs[0,1].set_title("Shoulder Touch : ")

axs[1,0].plot(B9)
axs[1,0].plot(F9)
axs[1,0].set_title("Hand 90 degree: ")

axs[1,1].plot(BB)
axs[1,1].plot(FB)
axs[1,1].set_title("Bottle 90 degree : ")

plt.show()



