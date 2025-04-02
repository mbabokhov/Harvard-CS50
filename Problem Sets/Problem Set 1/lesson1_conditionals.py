# # Compare integers that come from user input with 'if' statement
# x = int(input('What is x? '))
# y = int(input('What is y? '))

# if x < y:
#     print('x is less than y')
# elif x > y:
#     print('x is greater than y')
# else:
#     print('x is equal to y')

# # If these were instead 3 if statements, you would have to ask 3 questions each time. **if/elif/else are all mutually exclusive**


# # include an 'or' statement
# x = int(input('What is x? '))
# y = int(input('What is y? '))

# # if x < y or x > y:
# #     print('x is not equal to y')
# # else:
# #     print('x is equal to y')

# # use a not equal question
# if x == y:
#     print('x is  equal to y')
# else:
#     print('x is not equal to y')


# include an 'and' statement
score = int(input('What is your score? '))

# # use mathmatical ranges with an implicit 'and'
# if 100 >= score >= 90:
#     print('You got an A')
# elif 90 > score >= 80:
#     print('You got a B')
# elif 80 > score >= 70:
#     print('You got a C')
# elif 70 > score >= 60:
#     print('You got a D')
# else:
#     print('You got an F')

# use real world logic, scores won't typically be above 100. Works because the program is using if/elif logic. Program runs top to bottom, if the first if statement already resolves as false, don't need to check >=90 in subsequent lines.
if score >= 90:
    print('You got an A')
elif score >= 80:
    print('You got a B')
elif score >= 70:
    print('You got a C')
elif score >= 60:
    print('You got a D')
else:
    print('You got an F')
