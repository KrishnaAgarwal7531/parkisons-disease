import numpy as np
import matplotlib.pyplot as plt

arr = np.loadtxt("emg_data.csv")
plt.title("EMG Sensor Data")
plt.plot(arr)
plt.show()