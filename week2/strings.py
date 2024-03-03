# PYTHON STRINGS AND STRING METHODS
# create a string using double quotes
string1 = "Python Programming"
# create a string using single quotes
string1 = 'Python Programming'

# Accessing String Characters in Python
greet = "Hello"
# access the 1st index element
print(greet[1]) # "e"

# Negative indexing
# access character 4th last element
print(greet[-4]) # "e"

#Slicing -access range of chars in a string by ':' operator
greet = 'hello'
#access char from the index 1 to index 3
print(greet[1:4])

# Python Multiline String
message = '''
Never gonna give you up
Never gonner give you up
'''
print(message)

# Python String Operations

#1. Compare Two Strings
#done using the == operater
# returns True if equal, otherwise False
str1 = "Hello, World"
str2 = "I love Python"
str3 = "Hello, World"
# compare str1 and str2
print(str1 == str2)
# compare str1 and str3
print(str1 == str3)

#2. Join Two or More Strings(concatenation)
# done using the + operator
greet= "Hello,"
name = "Jack"
#using + operator
result = greet + name
print(result)

#3. Iterating through String
greet = "Hello"
for letter in greet:
    print(letter)

# String Membership Test
print('a' in 'program') # True
print('at' not in 'battle') # False


# Escape Sequences in Python
# are used to escape some special characters in a strring
# example = "He said, "What's there?" - this will throw an error

# escape double quoutes
example ="He said, \"What's there?\""
print(example)
# escape single quotes
example = 'He said, "What\'s there?"'
print(example)

#Python String Formatting(f-Strings)
# f-Strings make it easy to print values and variables
name = 'Cathy'
country = 'UK'
print(f'{name} is from {country}')



