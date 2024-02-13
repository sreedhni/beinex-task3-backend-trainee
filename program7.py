# Write a Python program to find palindromes in a given list of strings using Lambda.

is_palindrome = lambda s: s == s[::-1]
strings= []

length=int(input("enter the size of list:"))
for i in range(length):  
   name=input(f"enter {i} th element:")  
   strings.append(name) 
palindromes = list(filter(is_palindrome, strings))

print("Palindromes in the list:", palindromes)
