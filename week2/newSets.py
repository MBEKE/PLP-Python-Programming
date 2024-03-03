# Accept user input to create the first set of intergers
input_str1 = input("Enter the intergers separated by spaces for the first set: ")
# Split the input into a list of strings
input_list1 = input_str1.split()
# Convert each string in the list to an integer and store in a set
set1 = {int(num) for num in input_list1}

# Accept user input to create the second set of intergers
input_str2 = input("Enter the intergers separated by spaces for the second se: ")
# Split the input string into a list of strings
input_list2 = input_str2.split()
# Convert each string in the list to an integer and store
set2 = {int(num) for num in input_list2}

# Create a new set that contains only the elements that are common in the 2 sets
common_elements = set1 & set2
# Print the new set
print("Common elements in both sets: ", common_elements)