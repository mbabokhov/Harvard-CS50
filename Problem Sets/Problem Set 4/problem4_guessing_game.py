# In a file called game.py, implement a program that:

# Prompts the user for a level, n. If the user does not input a positive integer, the program should prompt again.
# Randomly generates an integer between 1 and n, inclusive, using the random module.
# Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.

# If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
# If the guess is larger than that integer, the program should output Too large! and prompt the user again.
# If the guess is the same as that integer, the program should output Just right! and exit.

# Still missing the option to re-prompt if the guess is too high or too low. Also get UnboundLocalError when inputting non-integers. Likely due to the global variables set in the main function. Need to learn about classes?
import sys
import random


def main():
    n = get_level()
    random_number = get_random(n)
    guess = get_guess()
    guess_game(guess, random_number)


def get_level():
    """Return int, n, from user input."""
    while True:
        try:
            n = int(input('Level: '))
        except (ValueError, NameError):
            pass
        if n <= 1:
            pass
        else:
            return n


def get_random(n):
    """Return int, random_int, randomly generated between 1 and n."""
    random_number = random.randint(1, n)
    print(f'Random number is {random_number}')
    return random_number


def get_guess():
    """Return positive int, guess, from second user input."""
    while True:
        try:
            guess = int(input('Guess: '))
        except (ValueError, NameError):
            pass
        if guess < 0:
            pass
        else:
            return guess


def guess_game(guess, random_number):
    """Compare random_number and guess, prompt user to guess again if not equal."""
    if guess < random_number:
        print('Too small!')
    elif guess > random_number:
        print('Too large!')
    else:
        sys.exit('Just right!')


main()


# # Test code for get_level()
# while True:
#     try:
#         n = int(input('Level: '))
#     except (ValueError, NameError):
#         pass
#     if n < 1:
#         pass
#     else:
#         break
# print(n)

# # Test code for get_level()
# import random
# n = int(input('Number? '))
# random_number = random.randint(1, n)
# print(random_number)
