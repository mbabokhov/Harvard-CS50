
# Run unit tests to check for bugs in code

def main():
    x = input('What is x? ')
    print('x squared is', square(x))


def square(n):
    return n * n


if __name__ == '__main__':
    main()
# But code as it stands can't accept letters or floats without crashing
# Test by making new program lesson5_test_calculator.py
