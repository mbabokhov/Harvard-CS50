# Runtime errors occur when inputs are typed incorrectly

# x = int(input('What is x? '))
# print(f'x is {x}')
# # Only works if the input is an integer

# # Use try and except keywords to handle errors

# try:  # try signifies the normal conditions
#     x = int(input('What is x? '))
#     print(f'x is {x}')
# except ValueError:  # except signifies the exceptionals, what to do if try fails
#     print('x is not an integer')

# # Not best practice to have try/except on more than 1 line of code
# try:
#     x = int(input('What is x? '))
# except ValueError:
#     print('x is not an integer')

# print(f'x is {x}')
# # But returns name error if input is a non-integer. Can't assign an error to a variable, so x has no value for the print statement.


# # Use keyword else for try/except. Similar use of else as if/elif/else conditionals.
# try:
#     x = int(input('What is x? '))
# except ValueError:
#     print('x is not an integer')
# else:
#     print(f'x is {x}')


# # Include a re-prompt feature using a loop.
# while True:  # Infinite loop
#     try:
#         x = int(input('What is x? '))
#     except ValueError:
#         print('x is not an integer')
#     else:
#         break  # Use break statement to stop the loop once errors aren't detected
# print(f'x is {x}')


# # Create a defined function
# def main():
#     x = get_int()
#     print(f'x is {x}')


# def get_int():
#     while True:  # Infinite loop
#         try:
#             x = int(input('What is x? '))
#         except ValueError:
#             print('x is not an integer')
#         else:
#             break
#     return x  # Instead of a print statement, returns the value of x to a main function


# main()


# # Improve implementation of the get_int() function
# def main():
#     x = get_int()
#     print(f'x is {x}')


# def get_int():
#     while True:  # Infinite loop
#         try:
#             x = int(input('What is x? '))
#         except ValueError:
#             print('x is not an integer')
#         else:
#             return x # Can use return as a break in a defined function


# main()


# # Use pass keyword to re-prompt the user, but doesn't print an error statement
# def main():
#     x = get_int()
#     print(f'x is {x}')


# def get_int():
#     while True:  # Infinite loop
#         try:
#             x = int(input('What is x? '))
#         except ValueError:
#             pass
#         else:
#             return x  # Can use return as a break in a defined function


# main()


# Specify the call of the get_int() function in main() to generalize the defined function (can use it later for more than just x). Useful for inputs.
def main():
    x = get_int('What is x? ')
    print(f'x is {x}')


def get_int(prompt):
    while True:  # Infinite loop
        try:
            x = int(input(prompt))
        except ValueError:
            pass
        else:
            return x  # Can use return as a break in a defined function


main()
