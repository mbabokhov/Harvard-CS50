# Input and output of files. Make a list to output.

# names = []

# for _ in range(3):
#     name = input('What is your name? ')
#     names.append(name)

# for name in sorted(names):
#     print(f'hello, {name}')
# But lose the names list every time the program is run.

# Use open function. Requires the name of the file to be opened and, optionally, how to open it.
# name = input('What is your name? ')
# # 'w' creates a file if it doesn't already exist
# file = open('names.txt', 'w')
# # .write method of file function, adds the name variable to the .txt file
# file.write(name)
# # closes and saves the file
# file.close()

# But because use the .write function, it completely replaces the text file each time. Need an append method.
# name = input('What is your name? ')

# # Use 'a' instead of 'w'. Appends inputs to bottom of the list.
# file = open('names.txt', 'a')
# file.write(name)
# file.close()
# But get everything stuck together - appends the strings directly together.
# Unlike print() function, 'a' doesn't add an extra new line automatically.

# name = input('What is your name? ')

# file = open('names.txt', 'a')
# # Use an f-string that adds a line break
# file.write(f'{name}\n')
# file.close()

# Rather than use file.close(), use with keyword. Tells Python to automatically open and close files.

# name = input('What is your name? ')

# with open('names.txt', 'a') as file:
#     file.write(f'{name}\n')


# Code that reads an existing file. Use 'r' argument to access a file.

# with open('names.txt', 'r') as file:
#     # .readlines() method of file function. Stores data as a variable as a list.
#     lines = file.readlines()

# for line in lines:
#     print('hello,', line.rstrip())

# More Pythonic version
# with open('names.txt', 'r') as file:
#     for line in file:
#         print('hello,', line.rstrip())

# Can use sort and other functions as files are read. Make an empty list, add stuff to it and sort.
names = []
# Don't need to specific 'r' when opening a file, is the default.
with open('names.txt') as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f'hello, {name}')
# Advantage is that you can sort through or process information in Python, without altering the original source file.
