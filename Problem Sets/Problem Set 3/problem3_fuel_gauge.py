# Fuel gauges indicate, often with fractions, just how much fuel is in a tank. For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank is 50% full, and 3/4 indicates that a tank is 75% full.

# In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. And if 99% or more remains, output F instead to indicate that the tank is essentially full.

# If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. (It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.

# Obtain the input fraction as strings and split into input_x and input_y variables.
while True:
    try:
        input_x, input_y = input('What fraction of fuel is left? ').split('/')

    except ValueError:  # Exception for non-number string inputs
        pass

    else:
        try:  # Convert string input into integer
            int_x, int_y = int(input_x), int(input_y)

        except ValueError:  # Exception for non-integers
            pass

        if int_x > int_y:  # Conditional for non-fractional inputs (>1)
            pass

        else:
            # Calculation of fractional input to percentage output
            percent_fuel = (int_x / int_y) * 100

            if percent_fuel >= 99:
                print('Tank is full')
            elif percent_fuel <= 1:
                print('Tank is empty')
            else:
                print(f'{percent_fuel:.0f}% fuel left')

            break
