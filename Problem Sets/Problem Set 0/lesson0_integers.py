# # Lesson 0 example from lecture for integers

# # Basic math with no input
# x = 1
# y = 2
# z = x + y
# print(z)

# # Calculation with inputs, to get variable z

# x = input('What is x? ')
# y = input('What is y? ')
# # Need to use int function of variables. Inputs default to strings.
# z = int(x) + int(y)
# print(z)

# # Calculation with inputs, without a z
# # Nest functions to automatically make the input an integer
# x = int(input('What is x? '))
# y = int(input('What is y? '))

# print(x + y)


# # Working with floats
# x = float(input('What is x? '))
# y = float(input('What is y? '))

# # print(x + y)

# # Rounding floats as the output
# x = float(input('What is x? '))
# y = float(input('What is y? '))

# z = round(x + y)
# print(f'{z:,}')  # Use an f-string to add a comma to make 1000 into 1,000


# # Using division
# x = float(input('What is x? '))
# y = float(input('What is y? '))
# z = round(x / y, 2)  # Rounding to 2 digits
# print(z)

# Using division, rounding with f-string
x = float(input('What is x? '))
y = float(input('What is y? '))
z = x / y
print(f'{z:.2f}')  # Rounding to 2 digits with an f-string
