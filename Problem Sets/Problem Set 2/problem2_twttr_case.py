# When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels, much like Twitter was originally called twttr. In a file called twttr.py, implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.

# Same as the snake case, can use the continue keyword to skip a vowel?
# Store vowels in a list?


# Ver 1: Brute force. Have an if statement with __contains__ for each vowel.
user_input = str(input('What do you want to twitterize? '))
for letter in user_input:
    if letter.lower().__contains__('a'):
        continue
    elif letter.lower().__contains__('e'):
        continue
    elif letter.lower().__contains__('i'):
        continue
    elif letter.lower().__contains__('o'):
        continue
    elif letter.lower().__contains__('u'):
        continue
    print(letter, end='')

# Ver 2: Another attempt with a list. Using if\in.
vowels = ['a', 'e', 'i', 'o', 'u',
          'A', 'E', 'I', 'O', 'U']

user_input = str(input('What do you want to twitterize? '))
for letter in user_input:
    if letter in vowels:
        continue
    print(letter, end='')

# Ver 3: Another attempt with a list. Using if\in but with the .lower() function to simplify the list.
vowels = ['a', 'e', 'i', 'o', 'u']

user_input = str(input('What do you want to twitterize? '))
for letter in user_input:
    if letter.lower() in vowels:
        continue
    print(letter, end='')


# # Test 1: Code from problem2_snake_case.py with the continue keyword. Continue used in this way will not print the character that matches the if statement.
# user_input = str(input('What is your camel case? '))
# for letter in user_input:
#     if letter.isupper():
#         continue
#     print(letter.lower(), end='')


# # Test 2: The conditional of the if statement is __contains__ function for the letter a. This test will remove any "a"s from an input.
# user_input = str(input('What do you want to twitterize? '))
# for letter in user_input:
#     if letter.__contains__('a'):
#         continue
#     print(letter, end='')


# # Test 3: The __contains__ function only accepts one arguement, so can't input multiple vowels. Make a list of vowels in upper and lower case and input the list into the __contains__ function.
# vowels = ['a', 'e', 'i', 'o', 'u',
#           'A', 'E', 'I', 'O', 'U']

# user_input = str(input('What do you want to twitterize? '))
# for letter in user_input:
#     if letter.__contains__(vowels):
#         continue
#     print(letter, end='')
# # Doesn't work. Can't input a list into __contains__


# # Test 4: Try the __contains__ input as a tuple.
# vowels = ('a', 'e', 'i', 'o', 'u',
#           'A', 'E', 'I', 'O', 'U')

# user_input = str(input('What do you want to twitterize? '))
# for letter in user_input:
#     if letter.__contains__(vowels):
#         continue
#     print(letter, end='')
# # Doesn't work. Tuples don't work either, has to be a string.


# # Test 5: Try making vowels strings with an or statment.
# vowels = 'a' or 'e' or 'i' or 'o' or 'u' or 'A' or 'E' or 'I' or 'O' or 'U'

# user_input = str(input('What do you want to twitterize? '))
# for letter in user_input:
#     if letter.__contains__(vowels):
#         continue
#     print(letter, end='')
# # Doesn't work. A bunch of vowels separated by 'or' is considered a tuple. Vowels with a comma is considered a list.
