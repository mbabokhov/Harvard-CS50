# Suppose that a machine sells bottles of cola for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

# Implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. Once the user has inputted at least 50 cents, output how many cents in change the user is owed. Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.

# Version 1: Sets the coins required and the coins allowed to be input. Starts a loop that subtracts the inserted coins (if they're valid) from the required coins (50) until reaching 0. If below zero, then returns the absolute in change.
print('Amount due: 50')
required_coins = 50
valid_coins = [25, 10, 5]
while required_coins > 0:
    inserted_coins = int(input('Insert coins: '))
    if inserted_coins not in valid_coins:
        continue
    required_coins -= inserted_coins
    if required_coins >= 0:
        print('Amount due: ' + str(required_coins))
    else:
        print('Change owed: ' + str(abs(required_coins)))


# # Test 1: Implement while True loop for inserting coins. Continue prompting if coins inserted are less than 50 and print remaining required, otherwise break. Doesn't keep track of change of coins.
# while True:
#     coins = int(input('Insert coin: '))
#     if coins < 50:
#         print('Amount due: ' + str(50 - coins))
#         continue
#     else:
#         break


# # Test 2: Implement a loop to add coins to a total until reaching 50.
# total_coins = 0
# while total_coins < 50:
#     inserted_coins = int(input('Insert coins: '))
#     total_coins += inserted_coins
#     print('Coins inserted: ' + str(total_coins))


# # Test 3: Reverse the numbers to count down from 50. Using != isn't ideal as function only stops when it hits exactly 0.
# required_coins = 50
# while required_coins != 0:
#     inserted_coins = int(input('Insert coins: '))
#     required_coins -= inserted_coins
#     print('Amount due: ' + str(required_coins))


# # Test 4: Change the while condition to > 0. Add a set of valid coins and a conditional to the loop to check for their use.
# print('Amount due: 50')
# required_coins = 50
# valid_coins = [25, 10, 5]
# while required_coins > 0:
#     inserted_coins = int(input('Insert coins: '))
#     if inserted_coins not in valid_coins:
#         continue
#     required_coins -= inserted_coins
#     if required_coins >= 0:
#         print('Amount due: ' + str(required_coins))
#     else:
#         print('Change owed: ' + str(abs(required_coins)))
