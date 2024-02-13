# Write a Python program to find if a given string starts with a given character using Lambda. 

starts_with = lambda string, char: string.startswith(char)

string = input("enter the string ;")
charactor = input("enter the test character ; ")
test= starts_with(string,charactor)
if test:
    print(f"The string starts with {charactor}")
else:
    print(f"The string is not starts with {charactor}")
