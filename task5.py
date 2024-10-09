import csv

filename = '/home/pi/ee347/lab-4-advanced-python-group-15/task5.csv'

# Open the file in write mode
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    while True:
        name = input("Enter a name (or type 'quit' to stop): ")
        if name.lower() == 'quit':
            break
        writer.writerow([name])

# Open the file in read mode
with open(filename, mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[0])