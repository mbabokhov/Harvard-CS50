# Designing custom functions


# # Define a function called incantation
# def incantation(phrase='revere the silent flame'):
#     print('Incant:', phrase)


# incantation()
# # Ask used for input
# creed = input('What is your philosophy? ')

# incantation(creed)


# def main():  # Define the main function
#     creed = input('What is your philosophy? ')
#     incantation(creed)


# def incantation(incant='presence of mind'):
#     print('Incant:', incant)


# main()  # Call the main function


# Using the return function
def calculation():
    x = int(input('What is x? '))
    print('x squared is', square(x))


def square(n):
    return n * n  # Can't just do n * n, need the return function


calculation()
