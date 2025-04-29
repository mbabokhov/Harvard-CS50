# Importing the test program implemented in lesson4_coding_libaries.py
# import sys

# from lesson4_coding_libraries import hello

# if len(sys.argv) == 2:
#     hello(sys.argv[1])

# But end up printing the default print statements as well. Because you have the main() function call at the bottom. The import command reads the entirety of the imported function.
# Using if __name__ == '__main__': main() removes the print commands from the original main function and only prints the user input from the command line.

# Try importing the goodbye function instead
import sys

from lesson4_coding_libraries import goodbye

if len(sys.argv) == 2:
    goodbye(sys.argv[1])
