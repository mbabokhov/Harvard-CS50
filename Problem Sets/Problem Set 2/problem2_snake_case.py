# In some languages, it’s common to use camel case (otherwise known as “mixed case”) for variables’ names when those names comprise multiple words, whereby the first letter of the first word is lowercase but the first letter of each subsequent word is uppercase. For instance, whereas a variable for a user’s name might be called name, a variable for a user’s first name might be called firstName, and a variable for a user’s preferred first name (e.g., nickname) might be called preferredFirstName.

# Python, by contrast, recommends snake case, whereby words are instead separated by underscores (_), with all letters in lowercase. For instance, those same variables would be called name, first_name, and preferred_first_name, respectively, in Python.

# In a file called camel.py, implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case. Assume that the user’s input will indeed be in camel case.


# Ver 1: Loop to print a camel case string with an underbar before the capital turned lowercase. All letters are printed as lowercase, but the underbar is on the right instead of the left. With user input
user_input = str(input('What is your camel case? '))
for letter in user_input:
    if letter.isupper():
        print('_', end='')
    print(letter.lower(), end='')


# # Test 1: Loop to print a string letter by letter
# user_input = 'hello'
# for letter in user_input:
#     print(letter)

# # Test 2: Loop to print a string as one word
# user_input = 'hello'
# for letter in user_input:
#     print(letter, end='')


# Program idea:
# 1. Loop through letters until hit a capital
# 2. Insert an underbar '_' between the captial
# 3. lowercase the capital

# # Test 3:: Loop to print a camel case string broken at the capital. Break keyword isn't useful - won't be able to access the information in the string afterwards.
# user_input = 'ashenSkies'
# for letter in user_input:
#     print(letter, end='')
#     if letter.isupper():
#         break

# # Test 4: Loop to print a camel case string with an underbar. But adds underbar after the capital, needs to be before.
# user_input = 'ashenSkies'
# for letter in user_input:
#     print(letter, end='')
#     if letter.isupper():
#         print('_', end='')

# # Test 5: Loop to print a camel case string with an underbar before the capital turned lowercase. But the original capital is still there (there is an extra letter - a pain to then go and delete it).
# user_input = 'ashenSkies'
# for letter in user_input:
#     print(letter, end='')
#     if letter.isupper():
#         print('_' + letter.lower(), end='')


# # Test 6: Loop to print a camel case string with an underbar before the capital turned lowercase. All letters are printed as lowercase, but the underbar is on the right instead of the left.
# user_input = 'ashenSkies'
# for letter in user_input:
#     print(letter.lower(), end='')
#     if letter.isupper():
#         print('_', end='')

# # Test 7: Loop to print a camel case string with an underbar before the capital turned lowercase. All letters are printed as lowercase, but the underbar is on the right instead of the left. With user input
# user_input = str(input('What is your camel case? '))
# for letter in user_input:
#     print(letter.lower(), end='')
#     if letter.isupper():
#         print('_', end='')
