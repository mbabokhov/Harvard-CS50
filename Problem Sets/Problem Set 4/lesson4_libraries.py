# Libraries are typically modules in Python. For reusability of code.

# # Use import keyword to gain access to Python modules. Import the random function.
# import random

# coin = random.choice(['heads', 'tails'])
# print(coin)

# # Use from keyword to specify what part of module you want to import.
# from random import choice

# coin = choice(['heads', 'tails'])
# print(coin)

# Advantage of importing the whole library is that no risk of overlap with other code or libraries. Random.choice() will always be in the scope of the random module.

# # Using the random.randint(a, b) to pull a random integer between a and b, inclusive.
# import random

# number = random.randint(1, 10)
# print(number)

# # Using random.shuffle(x). Takes a list and randomizes the order.
# import random

# cards = ['jack', 'queen', 'king']
# random.shuffle(cards)
# for card in cards:
#     print(card)


# # Statistics module.
# import statistics

# print(statistics.mean([100, 90]))


# # Command line arguments. Provide input only when executing the program.
# # Sys module. sys.argv - argument vector, list that the user input before hitting enter.
# import sys

# print('hello, my name is', sys.argv[1])
# # If just run this program without typing name in terminal, then get an IndexError.

# # Rewrite program with an exception
# import sys
# try:
#     print('hello, my name is', sys.argv[1])
# except IndexError:
#     print('Too few arguments')

# # Check if names were input
# import sys

# if len(sys.argv) < 2:
#     print('Too few arguments')
# elif len(sys.argv) > 2:
#     print('Too many arguments')
# else:
#     print('hello, my name is', sys.argv[1])

# # More sys module functionality. Separate checking for errors from the active code.
# # Exit program early if the input isn't correct. Use sys.exit
# import sys

# if len(sys.argv) < 2:
#     sys.exit('Too few arguments')
# elif len(sys.argv) > 2:
#     sys.exit('Too many arguments')
# else:
#     print('hello, my name is', sys.argv[1])

# # Use a loop to handle multiple inputs at the command line.
# import sys

# if len(sys.argv) < 2:
#     sys.exit('Too few arguments')

# for arg in sys.argv:
#     print('hello, my name is', arg)
# # But end up with the name of the program as an arg in the list.

# Resolve using a slice. Use square brackets [] of a list to specify a subset of the list. Start with location 1 to skip the name of the program.
import sys

if len(sys.argv) < 2:
    sys.exit('Too few arguments')

for arg in sys.argv[1:]:
    print('hello, my name is', arg)
