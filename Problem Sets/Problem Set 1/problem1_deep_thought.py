# In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.


# Using if/elif/else
answer = input(str(
    'What is the Answer to the Great Question of Life, the Universe and Everything? ')).lower()
if answer == '42':
    print('Yes')
elif answer == 'forty-two':
    print('Yes')
elif answer == 'forty two':
    print('Yes')
else:
    print('No')


# Using match/case
answer = input(str(
    'What is the Answer to the Great Question of Life, the Universe and Everything? ')).lower()

match answer:
    case '42' | 'forty two' | 'forty-two':
        print('Yes')
    case _:
        print('No')
