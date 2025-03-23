filename=input("Enter a file name: ")
try:
    with open(filename, 'r') as file:
        for line in file:
            print(line.upper(), end='')
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")