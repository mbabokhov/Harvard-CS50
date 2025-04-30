# Test program for testing the calculator program in lesson5_unit_tests.py

import pytest
from lesson5_unit_tests import square

# By convention, test functions should be named as test_ before the name of the function being tested.


# def main():
#     test_square()


# def test_square():
#     if square(2) != 4:
#         print('2 squared was not 4')
#     if square(3) != 9:
#         print('3 squared was not 9')


# if __name__ == '__main__':
#     main()

# Really want to automate the different test functions.
# Use the assert keyword. If assert and the assertation is false, get an error message.


# def main():
#     test_square()


# def test_square():
#     assert square(2) == 4
#     assert square(3) == 9


# if __name__ == '__main__':
#     main()

# Combine assert with try/exception keywords.
# def main():
#     test_square()


# def test_square():
#     try:
#         assert square(2) == 4
#     except AssertionError:
#         print('2 squared was not 4')
#     try:
#         assert square(3) == 9
#     except AssertionError:
#         print('3 squared was not 9')


# if __name__ == '__main__':
#     main()

# Can streamline and automate testing code by using the pytest library. Common for unit tests of functions in Python.

# def test_square():
#     assert square(2) == 4
#     assert square(3) == 9
#     assert square(-2) == 4
#     assert square(-3) == 9
#     assert square(0) == 0

# To run pytest: in terminal type 'pytest' followed by name of the test program.
# Output in the terminal window lists the assertions that passed and those that failed.
# Big reason to break up code into smaller functions. Can test them individually using pytest.

# However, test stops once it reaches the first failure case. Break down into different categories of tests using different functions.

def test_positive_square():
    assert square(2) == 4
    assert square(3) == 9


def test_negative_square():
    assert square(-2) == 4
    assert square(-3) == 9


def test_zero_square():
    assert square(0) == 0


# Testing for TypeErrors. Use the raises function from pytest library.


def test_str():
    with pytest.raises(TypeError):
        square('snail')
# This passes the pytest process. Confirms that if the user were to enter a str like 'snail', then the program will raise a TypeError.

# Can't test print functions this way. Because print functions don't return something.
# As a general rule avoid print functions in your defined functions. Save them for the main function.

# Example with a hello function:


def main():
    name = input('What is your name? ')
    print(hello(name))


def hello(to='world'):
    return f'hello, {to}'


if __name__ == '__main__':
    main()

# Can use a test like:


def test_hello_default():
    assert hello() == 'hello, world'


def test_hello_name():
    assert hello('Mike') == 'hello, Mike'
