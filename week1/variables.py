# variables are reserved mem loc used to store values in Python Program
# Python's built-in id() function returns the address of an object
month = "May"
age = 18
print(id(month))
print(id(age))

# Creating variables in Python
counter = 100  # creates an integer variable
miles = 1000.0 # creates a string variable 
name = "Brian Ogada"
# Printing  variables using the print() function
print(counter)
print(miles)
print(name)

#Deleting Python Variables
# syntax for deleting: del var1[,var2[,var3[....,varN]]]]
# Example: 
del counter
#print(counter)  # This will produce an error

#Getting Variable Type 
x = 'Zara'
y = 10
z = 10.10

print(type(x))
print(type(y))
print(type(z))