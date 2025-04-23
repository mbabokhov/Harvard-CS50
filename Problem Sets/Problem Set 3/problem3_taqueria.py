# In a file called taqueria.py, implement a program that enables a user to place an order, prompting them for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). After each inputted item, display the total cost of all items inputted thus far, prefixed with a dollar sign ($) and formatted to two decimal places. Treat the user’s input case insensitively. Ignore any input that isn’t an item. Assume that every item on the menu will be titlecased.

# Dictionary containing key:value pairs of food:price.
menu = {
    'Baja Taco': 4.25,
    'Burrito': 7.50,
    'Bowl': 8.50,
    'Nachos': 11.00,
    'Quesadilla': 8.50,
    'Super Burrito': 8.50,
    'Super Quesadilla': 9.50,
    'Taco': 3.00,
    'Tortilla Salad': 8.00
}


def main():
    order_cost = get_order('What is your order? ')
    print(end='\n')


def get_order(prompt):
    order_cost = 0.0
    while True:
        try:
            order = input(prompt).title()
        except EOFError:
            break
        else:
            if order in menu:
                order_cost += menu[order]
                print(f'Order cost: ${order_cost:.2f}')


main()
