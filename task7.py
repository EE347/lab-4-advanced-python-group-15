import numpy as np

x = np.linspace(0, 10, 101)
sin_x = np.sin(x)
cos_x = np.cos(x)

np.save('/home/pi/ee347/lab-4-advanced-python-group-15/task7_sin.npy', sin_x)
np.save('/home/pi/ee347/lab-4-advanced-python-group-15/task7_cos.npy', cos_x)

print("Sine and cosine waves have been saved.")