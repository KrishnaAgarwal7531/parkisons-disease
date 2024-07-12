
import pandas as pd

arr = pd.read_csv("noise_trial.csv",skiprows=1)
avg =arr.mean()

for i,a in enumerate(avg):
    print(i+1,a)

'''''

import numpy as np 
import matplotlib.pyplot as plt

arr = np.loadtxt("noise_trial.csv",delimiter=',')

AX = arr[:,0]
AY = arr[:,1]
AZ = arr[:,2]
GX = arr[:,3]
GY = arr[:,4]
GZ = arr[:,5]

print(AX.mean())
print(AY.mean())
print(AZ.mean())
print(GX.mean())
print(GY.mean())
print(GZ.mean())
'''''