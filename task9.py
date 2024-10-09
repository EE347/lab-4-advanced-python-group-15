import csv
import matplotlib.pyplot as plt
from datetime import datetime

# File path
file_path = '/home/pi/ee347/lab-4-advanced-python-group-15/task9.csv'

# Lists to store the data
dates = []
values = []

# Read the CSV file
with open(file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)  # Skip the header row
    for row in csvreader:
        dates.append(datetime.strptime(row[0], '%d/%m/%Y'))
        values.append(float(row[1]))

# Plot the data
plt.figure(figsize=(10, 5))
plt.plot(dates, values, marker='o')
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Data from task9.csv')
plt.grid(True)
plt.show()