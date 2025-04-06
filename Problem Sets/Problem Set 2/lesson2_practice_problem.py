# # Simple way to print a column
# print('#')
# print('#')
# print('#')

# # Use a for loop
# for _ in range(3):
#     print('#')

# # Define a function


# def main():
#     print_column(3)


# def print_column(height):
#     for _ in range(height):
#         print('#')


# main()


# # Re-define a function


# def main():
#     print_column(3)


# def print_column(height):
#     print('#\n' * height, end='')


# main()

# # Abstract to include horizontal rows


# def main():
#     print_row(4)


# def print_row(width):
#     print('?' * width)


# main()


# Use the function to display a 2D object with an outer and an inner loop:

def main():
    print_square(3)


def print_square(size):
    # For each row in square
    for i in range(size):  # Convention to use i and j in nested loops
        # For each brick in row
        for j in range(size):
            # Print brick
            print('#', end='')
        print()  # Below inner loop. Once each inner loop is done print a blank line (same as printing a \n)


main()
