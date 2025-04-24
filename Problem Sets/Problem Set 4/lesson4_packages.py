# Packages are 3rd party libraries. Module implemented as a folder and not just a file.
# Get them at pypi.org

# pip is a package manager program that installs packages using a command
# Can import packages through the command line
# To install package cowsay type: 'pip install cowsay' in the command line
# Can update pip by typing 'python.exe -m pip install --upgrade pip' in the command line

# import cowsay
# import sys

# if len(sys.argv) == 2:
#     cowsay.trex('hello, ' + sys.argv[1])

# API: application programming interface. 3rd party services that can be communicated with using Python. Typically on servers on the internet.
# requests library. Use python code to access open source code on the internet. Using code like a browser. Very commonly used.
# Type 'pip install requests' in the command line to install.

# Apple API
# In a browser would type: https://itunes.apple.com/search?entity=song&limit=1&term=weezer. Get a text file downloaded.
# JSON (Java Script Object Notation) is a language-agnostic format to exchange data between computers. Completely text based.
# Write Python code that replicates what the browser does.
# import requests
# import sys

# if len(sys.argv) != 2:
#     sys.exit()

# response = requests.get(
#     'https://itunes.apple.com/search?entity=song&limit=1&term=' + sys.argv[1])
# print(response.json())

# Prints the JSON file formatted as a Python dictionary
# Can format JSON data with the json library
# import json
# import requests
# import sys

# if len(sys.argv) != 2:
#     sys.exit()

# response = requests.get(
#     'https://itunes.apple.com/search?entity=song&limit=1&term=' + sys.argv[1])
# print(json.dumps(response.json(), indent=2))

# Iterate over the dictionary provided to grab the track name out of the dictionary.
import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get(
    'https://itunes.apple.com/search?entity=song&limit=50&term=' + sys.argv[1])
print(json.dumps(response.json(), indent=2))

_ = response.json()
for result in _['results']:
    print(result['trackName'])
