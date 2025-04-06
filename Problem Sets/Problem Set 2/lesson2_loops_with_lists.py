electors = ['Silverforge', 'Damescrown', 'Istralore']

# # use square brackets to index into a list. Python lists are 0-indexed
# print(electors[0])
# print(electors[1])
# print(electors[2])

# # Use a for loop to automatically index a list
# for elector in electors:
#     print(elector)


# # Using numbers with the len function to get the length of a list

# # len function assigns a number to each item of a list
# print(len(electors))
# for number in range(len(electors)):
#     # print(electors[number])
#     # can print both the len and the corresponding str:
#     print(number, electors[number])


# # Another data type: dictionaries 'dict'. Can associate one value with another. Keys associated with values.

# # Use curly braces {} for dictionaries, different application than {} for f-strings

# nations = {
#     'Asheniande': 'Moon',
#     'Silverforge': 'Moon',
#     'Saloren': 'Moon',
#     'Wex': 'Rose'
# }

# # # Index into a dictionary. Lists have numberic indecies (0, 1, 2). Dictionaries use words as indecies
# # print(nations['Asheniande'])
# # print(nations['Saloren'])
# # print(nations['Silverforge'])
# # print(nations['Wex'])

# # Use a for loop to iterate over a dictionary. For loops always return keys as default
# for nation in nations:
#     print(nation, nations[nation], sep=', ')
#     # Syntax of nations[nation] indexes the dictionary, gives the value for the key to print as part of the loop


# Adding an additional value to the key. Make a list of dictionaries

nations = [
    {'name': 'Asheniande', 'party': 'Moon', 'culture': 'Arranese'},
    {'name': 'Silverforge', 'party': 'Moon', 'culture': 'Silver Dwarf'},
    {'name': 'Saloren', 'party': 'Moon', 'culture': 'Rosilardi'},
    {'name': 'Wex', 'party': 'Rose', 'culture': None}  # Suck it Wex
]
# 3 keys: name, party, culture with 3 values per key per nation

for nation in nations:  # loop that iterates over nations in the list
    print(nation['name'], nation['party'], nation['culture'], sep=', ')
