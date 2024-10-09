def read_and_print_names(file_path):
    try:
        with open(file_path, 'r') as file:
            names = file.readlines()
            for name in names:
                print(name.strip())
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")

if __name__ == "__main__":
    file_path = '/home/pi/ee347/lab-4-advanced-python-group-15/task3.txt'  
    read_and_print_names(file_path)