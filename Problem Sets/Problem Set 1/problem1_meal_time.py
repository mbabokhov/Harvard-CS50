# Suppose that you’re in a country where it’s customary to eat breakfast between 7:00 and 8:00, lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00. Wouldn’t it be nice if you had a program that could tell you what to eat when?

# In meal.py, implement a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time. If it’s not time for a meal, don’t output anything at all. Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##. And assume that each meal’s time range is inclusive. For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.

def main():
    user_input = str(input('What time is it? '))
    if 8.0 >= convert(user_input) >= 7.0:
        print('It is breakfast time.')
    elif 13.0 >= convert(user_input) >= 12.0:
        print('It is lunchtime.')
    elif 19.0 >= convert(user_input) >= 18.0:
        print('It is dinner time.')


# Define a convert function based on test case below. Takes a 24hr time and splits into the hours and minutes. Converts the hour into a float. Then converts the minutes into a float of the fraction of an hour. Then adds the two numbers as the variable converted_time.


def convert(time):
    hours, minutes = time.split(':')
    converted_time = float(hours) + (float(minutes) / 60)
    return converted_time

# The convert function returns a converted_time variable. This is a float that can be placed in a range of the main function. Which range it fits into determines the meal time. The main function uses the convert function on the user_input directly in the range calculation.


main()


# # Testing out code for convert function. Check independently before incorporating it into a defined function.
# user_input = str(input('What time is it? '))

# hours, minutes = user_input.split(':')
# print(hours)
# print(minutes)
# converted_time = float(hours) + (float(minutes) / 60)
# print(converted_time)
