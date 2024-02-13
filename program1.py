gg# Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, 
# also create a lambda function that multiplies argument x with argument y and prints the result

add= lambda x: x + 15

multiply= lambda x, y: print(x * y)

num1 = float(input("enter a number for add: "))
print(add(num1))
num2=float(input("enter a number1 for multiply: "))
num3=float(input("enter a number2 for multiply: "))

(multiply(num2, num3))
