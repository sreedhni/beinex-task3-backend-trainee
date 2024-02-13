# Write a Python program to check whether a given string is a number or not using Lambda
check_numbers = lambda x: x.isdigit()

string = input("Enter a string: ")

if check_numbers(string):
    print("The string consists of all numbers.")
else:
    print("The string contains non-numeric characters.")
