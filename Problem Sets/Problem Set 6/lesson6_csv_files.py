# Comma seperated values (CSV) files. See files names.csv for this lesson.

# # Access across the 'columns' of comma separated data. Use row/column as names by convention.
# with open('names.csv') as file:
#     for line in file:
#         row = line.rstrip().split(',')
#         print(f'{row[0]} has a lot of {row[1]}')

# # Unpacking rows from a CSV. Automatically assign multiple variables to data extacted from CSV files.
# with open('names.csv') as file:
#     for line in file:
#         name, race = line.rstrip().split(',')
#         print(f'{name} has a lot of {race}')

# # Sorting csv outputs. Add the csv output to an empty list.
# nations = []
# with open('names.csv') as file:
#     for line in file:
#         name, race = line.rstrip().split(',')
#         nations.append(f'{name} has a lot of {race}')

# for nation in sorted(nations):
#     print(nation)

# # Better way to do organize by using a temporary dictionary. Add the csv columns as key:value pairs in the dictionary.
# nations = []
# with open('names.csv') as file:
#     for line in file:
#         name, race = line.rstrip().split(',')
#         nation = {}
#         nation['name'] = name
#         nation['race'] = race
#         nations.append(nation)

# for nation in nations:
#     print(f'{nation['name']} has a lot of {nation['race']}')

# # Simpler version. Make the dictionary and assign the key:value pairs at the same time.
# nations = []
# with open('names.csv') as file:
#     for line in file:
#         name, race = line.rstrip().split(',')
#         nation = {'name': name, 'race': race}
#         nations.append(nation)

# for nation in nations:
#     print(f'{nation['name']} has a lot of {nation['race']}')

# # Sorting. Sort a list by looking at a specific key in a dictionary. Use key parameter. Can pass functions as arguments of other functions.
# nations = []
# with open('names.csv') as file:
#     for line in file:
#         name, race = line.rstrip().split(',')
#         nation = {'name': name, 'race': race}
#         nations.append(nation)


# def get_name(nation):
#     return nation['name']


# for nation in sorted(nations, key=get_name):
#     print(f'{nation['name']} has a lot of {nation['race']}')

# # Remove the defined get_name function and use a lambda function instead. Lambdas are anonymous functions with no defined name (because only used in one place). Similar to the use of _ as a one-time variable name.
# nations = []
# with open('names.csv') as file:
#     for line in file:
#         name, race = line.rstrip().split(',')
#         nation = {'name': name, 'race': race}
#         nations.append(nation)

# for nation in sorted(nations, key=lambda nation: nation['name']):
#     print(f'{nation['name']} has a lot of {nation['race']}')

# Additional commas in the csv file leaves a ValueError.
nations = []
with open('more_names.csv') as file:
    for line in file:
        name, race = line.rstrip().split(',')
        nation = {'name': name, 'race': race}
        nations.append(nation)

for nation in sorted(nations, key=lambda nation: nation['name']):
    print(f'{nation['name']} has a lot of {nation['race']}')

# 8:01 to continue
