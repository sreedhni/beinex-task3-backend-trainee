# Write a Python program to create a function that takes one argument, and that argument will be
# multiplied with an unknown given number. 0

def multiply(number):
    unknown_num= float(input("enter a unknownnumber"))  
    return number * unknown_num

argument = float(input("enter a number as argumnt:"))
result = multiply(argument)
print("Result:", result)
