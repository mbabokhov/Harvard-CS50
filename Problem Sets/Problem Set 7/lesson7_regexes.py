# Define patterns in code and compare them to data that the program is receiving.
# Example without any regular expressions, for checking email input as valid:

# email = input('What is your email? ').strip()

# user_name, domain = email.split('@')

# if user_name and '.' in domain:
#     print('Valid')
# else:
#     print('Invalid')

# Have the re libary for regular expression to define and check for patterns.
# re.search() function. Can pass a pattern to search for, a string to be searched, and optional flag arguments.

import re

# email = input('What is your email? ').strip()

# # Can simply search for a str in an input

# if re.search('@', email):
#     print('Valid')
# else:
#     print('Invalid')

# When using regular expressions can use symbols to define patterns:
# . indicates any character besides new line. Here represents any text before the @ sign in an email.
# However, just a . could accept one character. Use .* to indicate zero or more than one.
# Use .+ to indicate one or more. ..* also technically equivalent.

# email = input('What is your email? ').strip()

# if re.search('.+@.+', email):
#     print('Valid')
# else:
#     print('Invalid')

# Check for .edu at the str end as well. Use escape character \ to specifiy the string '.edu'. Use a raw string r'str' to specifiy the function of the escape character. Without the raw string, the program would accept \edu as valid.

# email = input('What is your email? ').strip()

# if re.search(r'.+@.+\.edu', email):
#     print('Valid')
# else:
#     print('Invalid')

# Good practice to always use r-strings in regular expressions.

# More regex symbols: ^ to set the start of the string, $ to set the end of the string.
# re.search will look for an exact match any pattern between ^   $.

# email = input('What is your email? ').strip()

# if re.search(r'^.+@.+\.edu$', email):
#     print('Valid')
# else:
#     print('Invalid')

# More regex symbols: [] to define a specific set of characters. [^] to define a set of characters to refuse.
# Replace . with [^@]. Instead of any character represented by . replace with any character except @ represented by [^@].

# email = input('What is your email? ').strip()

# if re.search(r'^[^@]+@[^@]+\.edu$', email):
#     print('Valid')
# else:
#     print('Invalid')

# More restrictions on the input. Specifiy range in square brackets [] with hyphen -, no spaces to separate.

# email = input('What is your email? ').strip()

# if re.search(r'^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$', email):
#     print('Valid')
# else:
#     print('Invalid')

# re library has common symbols for frequently used patterns. \w stands for words, equivalent to [a-zA-Z0-9_]
# Also have: \d - decimal digit, \D - not decimal digit, \s - whitespace, \S - not whitespace.

# email = input('What is your email? ').strip()

# if re.search(r'^\w+@\w+\.edu$', email):
#     print('Valid')
# else:
#     print('Invalid')

# Can configure re.search with optional flag arguments.
# re.IGNORECASE, re.MULTILINE, re.DOTALL

# email = input('What is your email? ').strip()

# if re.search(r'^\w+@\w+\.edu$', email, re.IGNORECASE):
#     print('Valid')
# else:
#     print('Invalid')

# Can have multiple potential inputs: A|B , A or B. Use parentheses () to group or expressions.

email = input('What is your email? ').strip()

if re.search(r'^\w+@(\w+\.)?\w+\.edu$', email, re.IGNORECASE):
    print('Valid')
else:
    print('Invalid')
