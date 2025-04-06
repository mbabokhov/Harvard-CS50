# Formatting loops with user inputs
# If you want user input to match the expected value that lets the program run. Use a while True:. Induce an infinite loop

# while True:
#     number = int(input('How many vais? '))
#     if number < 0:
#         continue # If user inputs a negative number (which you don't want), make the program loop the input. Using the continue keyword
#     else:
#         break # Keyword that stops the loop

# # Cleaner way, common paradigm for inputs
# while True:
#     # Loops the input until the user gives a number greater than 0
#     number = int(input('How many vais? '))
#     if number > 0:
#         break  # Keyword that stops the loop once you get a positive number

# for _ in range(number):
#     print('vai')


# Introduce a defined function

def main():
    number = get_number()
    vai(number)


def get_number():
    while True:
        number = int(input('How many vais? '))
        if number > 0:
            return number


def vai(number):
    for _ in range(number):
        print('vai')


main()
