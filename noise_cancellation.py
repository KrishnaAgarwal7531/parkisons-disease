import numpy as np 
import matplotlib.pyplot as plt

arr = np.loadtxt("noise_trial2.csv",delimiter=',')

AX = arr[:,0]
AY = arr[:,1]
AZ = arr[:,2]
GX = arr[:,3]
GY = arr[:,4]
GZ = arr[:,5]

plt.plot(AX)
plt.plot(AY)
plt.plot(AZ)
plt.plot(GX)
plt.plot(GY)
plt.plot(GZ)
plt.show()



