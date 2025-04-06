# Loop using the "while" keyword, uses boolean logic, continues an action until a condition is either true or false

# set a variable and then ask the while question

# count = 3
# while count != 0:
#     print('vai')
#     count = count - 1  # very important to set a change, otherwise count will always be 3 and you get an infinite loop

# # an example when you count up
# count = 1
# while count <= 3:
#     print('vai')
#     count = count + 1

# # as a convention start your counts from 0
# count = 0
# while count < 3:
#     print('vai')
#     # count = count + 1
#     count += 1  # same as above


# # Loop using the "for/in" keywords. also incorporating the "list" datatype. allows iteration over a list of items
# for count in [0, 1, 2]:  # use square brackets [] for lists
#     print('vai')

# # use a range function in the list to generalize
# for count in range(3):
#     print('vai')

# as a Pythonic option name the variable as '_', but isn't used later, just to set the loop
for _ in range(3):
    print('vai')
