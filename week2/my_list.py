# Create empty list
my_list = []
# append elements to the list
my_list.extend([10, 20, 30, 40])
# insert value '25' at the 2nd position in the list
my_list.insert(1, 15)
# extend my_list with another list: [50, 60, 70]
my_list.extend([50, 60, 70])
# remove the last element from my_list
del my_list[-1]
# sort my_list in ascending order
my_list.sort()
# find and print the index of the value 30 in my_list
index_of_30 = my_list.index(30)
#Print the modified my_list and the index of 30
print(f'The modified my_list: {my_list}')
print(f'Index of 30: {index_of_30}')

