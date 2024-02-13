# Write a Python program to find the maximum value in a given heterogeneous list 
# using lambda.Original list: 

# ['Python', 3, 2, 4, 5, 'version']

original_list = ['Python', 3, 2, 4, 5, 'version']

max_value = max(filter(lambda x: isinstance(x, int), original_list), default=None)
print("Maximum value in the list:", max_value)
