# Python already supports math, whereby you can write code to add, subtract, multiply, or divide values and even variables. But let’s write a program that enables users to do math, even without knowing Python.

# In a file called interpreter.py, implement a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place. Assume that the user’s input will be formatted as x y z, with one space between x and y and one space between y and z, wherein:

# x is an integer
# y is +, -, *, or /
# z is an integer

# For instance, if the user inputs 1 + 1, your program should output 2.0. Assume that, if y is /, then z will not be 0.

# Note that, just as python itself is an interpreter for Python, so will your interpreter.py be an interpreter for math!

input_expresion = str(input('What is your expression? '))

# Use .split method to get the input expression as three different strings
first_number, operator, second_number = input_expresion.split(' ')

# # Can confirm the strings and their type with print functions
# print(first_number, operator, second_number)
# print(first_number)
# print(type(first_number))
# print(operator)
# print(type(operator))
# print(second_number)
# print(type(second_number))

# Use if/elif/else. Detect the string of the operator type and assign 4 variables: add for '+', subtract for '-', multiply for '*' and divide for '/'. Perform the corresponding math, converting the string to a float. Print using an f-string to round to 1 decimal place.

if operator == '+':
    add = float(first_number) + float(second_number)
    print(f'{add:.1f}')
elif operator == '-':
    subtract = float(first_number) - float(second_number)
    print(f'{subtract:.1f}')
elif operator == '*':
    multiply = float(first_number) * float(second_number)
    print(f'{multiply:.1f}')
elif operator == '/':
    divide = float(first_number) / float(second_number)
    print(f'{divide:.1f}')
else:
    print('Could not compute. Please input expression as two numbers with one operator (+, -, *, /). Ex. 1 + 1')
