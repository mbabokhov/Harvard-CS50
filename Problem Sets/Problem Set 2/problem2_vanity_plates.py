# n Massachusetts, home to Harvard University, it’s possible to request a vanity license plate for your car, with your choice of letters and numbers instead of random ones. Among the requirements, though, are:

# “All vanity plates must start with at least two letters.”
# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
# “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
# “No periods, spaces, or punctuation marks are allowed.”

# In plates.py, implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not. Assume that any letters in the user’s input will be uppercase. Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not. Assume that s will be a str. You’re welcome to implement additional functions for is_valid to call (e.g., one function per requirement).


# Ver 1: Best try. Ran the last 3 conditionals in one line linked by "or" "and" operators. However, depends on call at position of 2 being non-zero. So AAA05 will be mistakenly output as valid.
def main():
    plate = input("What would you like your plate to be?: ")
    if is_valid(plate):
        print("This plate is valid")
    else:
        print("This plate is invalid")


def is_valid(plate_string):
    if plate_string[0:2].isalpha() and plate_string.isalnum():
        if 6 >= len(plate_string) >= 2:
            if plate_string.isalpha() or plate_string[-1].isnumeric() and plate_string[2] != '0':
                return True
    else:
        return False


main()


# # Test 1: Checking for the first two characters as letters using the .isalpha() function and the length with the len() function. The two conditionals don't work because the second is inaccessible - it's after the return statement.
# def main():
#     plate = input("What would you like your plate to be?: ")
#     if is_valid(plate):
#         print("This plate is valid")
#     else:
#         print("This plate is invalid")


# def is_valid(plate_string):
#     if plate_string[0:2].isalpha():
#         return True
#     else:
#         return False
#     if 6 >= len(plate_string) >= 2:
#         return True
#     else:
#         return False


# main()


# # Test 2: Making the second conditional accessible by nesting it in the first and placing the True/False last. Nesting works.
# def main():
#     plate = input("What would you like your plate to be?: ")
#     if is_valid(plate):
#         print("This plate is valid")
#     else:
#         print("This plate is invalid")


# def is_valid(plate_string):
#     if plate_string[0:2].isalpha():
#         if 6 >= len(plate_string) >= 2:
#             return True
#     else:
#         return False


# main()


# # Test 3: Adding the 3rd nested conditional - either position 3 cannot be a number or the whole thing is letters or position 3 is a letter. Problems with the if an elif statements lining up before the return.
# def main():
#     plate = input("What would you like your plate to be?: ")
#     if is_valid(plate):
#         print("This plate is valid")
#     else:
#         print("This plate is invalid")


# def is_valid(plate_string):
#     if plate_string[0:2].isalpha():
#         if 6 >= len(plate_string) >= 2:
#             if plate_string[-1].isnumeric():
#             elif plate_string.isalpha():
#                 # if plate_string[3].isalpha():
#                 return True
#     else:
#         return False


# main()


# Test 4: Try elifs.


# def main():
#     plate = input("What would you like your plate to be?: ")
#     if is_valid(plate):
#         print("This plate is valid")
#     else:
#         print("This plate is invalid")


# def is_valid(plate_string):
#     if plate_string[0:2].isalpha():
#         if 6 >= len(plate_string) >= 2:
#             if plate_string[-1].isnumeric():
#             elif plate_string.isalpha:
#             elif plate_string[2].isalpha():
#                 return True
#     else:
#         return False


# main()
