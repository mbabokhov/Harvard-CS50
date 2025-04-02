# use the modulo operator % to calculate a remainder in division. answer if number is even or odd

# x = int(input('What is x? '))

# if x % 2 == 0:
#     print('x is even')
# else:
#     print('x is odd')

# define a function that calculates even or odd

# first define the main function that takes user input and runs a nested function


# def main():
#     x = int(input('What is x? '))
#     if is_even(x):
#         print('x is even')
#     else:
#         print('Odd')

# # define the nested function that checks for even or odd
# # is_even returns True for even numbers, otherwise False for odd numbers


# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False


# main()


# re-write code to make it more 'Pythonic'. rewrite the code to utilize more features that are exclusive to the Python language.


# first define the main function that takes user input and runs a nested function
def main():
    x = int(input('What is x? '))
    if is_even(x):
        print('x is even')
    else:
        print('Odd')

# define the nested function that checks for even or odd
# is_even returns True for even numbers, otherwise False for odd numbers

# # Pythonic definition version 1
# def is_even(n):
#     return True if n % 2 == 0 else False

# Pythonic definition version 2. the math is boolean anyways. Answer will either be ==0 and thus be True, or !=0 and thus be False


def is_even(n):
    return n % 2 == 0


main()
