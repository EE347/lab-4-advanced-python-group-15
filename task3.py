
def append_name_to_file():
    with open('task3.txt', 'a') as file:
        for _ in range(3):
            name = input("Please enter your name: ")
            file.write(name + '\n')

if __name__ == "__main__":
    append_name_to_file()