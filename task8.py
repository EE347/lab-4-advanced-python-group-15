import numpy as np
import matplotlib.pyplot as plt

# Load the .npy files
sin_values = np.load('/home/pi/ee347/lab-4-advanced-python-group-15/task7_sin.npy')
cos_values = np.load('/home/pi/ee347/lab-4-advanced-python-group-15/task7_cos.npy')

# Create an x-axis for plotting
x = np.linspace(0, 10, num=len(sin_values))

# Plot the sine and cosine values
plt.figure(figsize=(10, 5))
plt.plot(x, sin_values, label='sin(x)', color='blue')
plt.plot(x, cos_values, label='cos(x)', color='orange')

# Add labels and title
plt.title('Sine and Cosine Functions')
plt.xlabel('x')
plt.ylabel('Value')
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.axvline(0, color='black',linewidth=0.5, ls='--')
plt.grid()
plt.legend()

# Show the plot
plt.show()
