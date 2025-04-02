# input an Anbennar nation and get the ruling house
nation = input('What is your nation? ')

# if nation == 'Asheniande':
#     print('sil Vivin')
# elif nation == 'Corvuria':
#     print('sil Vivin')
# elif nation == 'Ravenmarch':
#     print('sil Vivin')
# elif nation == 'Lorent':
#     print('Siloriel')
# else:
#     print('Where?')

# compound the nations with the same house

# if nation == 'Asheniande' or nation == 'Corvuria' or nation == 'Ravenmarch':
#     print('sil Vivin')
# elif nation == 'Lorent':
#     print('Siloriel')
# else:
#     print('Where?')

# use match/case as a different version. use 'case _:' instead of else

# match nation:
#     case 'Asheniande':
#         print('sil Vivin')
#     case 'Corvuria':
#         print('sil Vivin')
#     case 'Ravenmarch':
#         print('sil Vivin')
#     case 'Lorent':
#         print('Siloriel')
#     case _:
#         print('Where?')

# make the match/case statement more compact. use a | in between names as an or equivalent

match nation:
    case 'Asheniande' | 'Corvuria' | 'Ravenmarch':
        print('sil Vivin')
    case 'Lorent':
        print('Siloriel')
    case _:
        print('Where?')
