# Accept user input to create a list of integers
input_str = input("Enter a list of integers separated by spaces: ")
# Split the input string inot a list of strings
input_list = input_str.split()
# Initialze an empty list to store intergees
integer_list = []
#convert each string in the list to an interger and append to integer_list
for num_str in input_list:
    try:
        num = int(num_str)
        integer_list.append(num)
    except ValueError:
        print("Error: '{}' is not a valid integer.".format(num_str))
# Compute the sum of all the intergers in the list
sum_of_integers = sum(integer_list)
# Print the sum
print("Sum of all the integers:", sum_of_integers)
