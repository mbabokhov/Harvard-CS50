# Making your own Python modules by bundling up other blocks of code.

# Simple test functions:
def main():
    hello('world')
    goodbye('world')


def hello(name):
    print(f'hello, {name}')


def goodbye(name):
    print(f'goodbye, {name}')


# main()
# Calling main() like this causes problems when importing. Instead use:

if __name__ == '__main__':
    main()
