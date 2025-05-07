# CSV module. Reader function that automatically analyzes a csv file for commas etc. Reader returns a zero-indexed list.

import csv

# nations = []

# with open('more_names.csv') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         nations.append({'name': row[0], 'race': row[1]})

# for nation in sorted(nations, key=lambda nation: nation['name']):
#     print(f'{nation['name']} has a lot of {nation['race']}')

# Dictionary reader function .DictReader(). Returns a dictionary instead of a list. But need to include on row 1 the keys for the data.

# nations = []

# with open('more_names.csv') as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         nations.append({'name': row['name'], 'race': row['race']})

# for nation in sorted(nations, key=lambda nation: nation['name']):
#     print(f'{nation['name']} has a lot of {nation['race']}')

# Writing csv files using the csv.writer() function.

# nation = input('What is your tag? ')
# race = input('What is your race? ')

# with open('more_names.csv', 'a') as file:
#     writer = csv.writer(file)
#     writer.writerow([nation, race])

# Writing using a dictionary with csv.DictWriter(). Using fieldnames= as an argument for the positioning of columns in the resulting csv file.

nation = input('What is your tag? ')
race = input('What is your race? ')

with open('more_names.csv', 'a') as file:
    writer = csv.DictWriter(file, fieldnames=['nation', 'race'])
    writer.writerow({'nation': nation, 'race': race})
