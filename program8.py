# Write a Python program that multiplies each number in a list with a given number using lambda functions.
#  Print the results. 

original_list = [2, 4, 6, 9, 11]
given_number = 2

result = list(map(lambda x: x * given_number, original_list))

print("Results after multiplication:", result)
