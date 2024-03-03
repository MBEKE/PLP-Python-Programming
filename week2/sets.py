# SET - a collection of unique data, elements of a set cannot be duplicated
# can have any no. of items & they may be of different types
# cannot have mutable elements like lists,sets or dictionaries as its elements

# create a set of integer type
student_id = {112, 114, 116, 118, 115}
print('Student ID:', student_id)

# create a set of string type
vowel_letters = {'a', 'e', 'i', 'o', 'u'}
print('Vowel Letters:', vowel_letters)

# create a set mixed data types
mixed_set = {'Hello', 101, -2, 'Bye'}
print('Set of mixed data types:', mixed_set)

# CREATE EMPTY SET IN PYTHON
# we use the set() function to make empty set

empty_set = set()

# create empty dictionary
empty_dictionary = {}

#check data type of empty_set
print('Data type of empty_set:', type(empty_set))

#check data type of dictionary_set
print('Data type of empty_dictinary:', type(empty_dictionary))

# DUPLICATE ITEMS IN A SET
# no duplicate items in the set is allowed eg.
numbers = {2, 4, 6, 6, 2, 8}
print(numbers) #{8, 2, 4, 6}

# ADD & UPDATE SET ITEMS IN PYTHON
# sets are mutable, however since they are unorderd, inedexing has no meaning

# adding items to set using add()
ages = {21, 34, 45, 12}

#using add() method
ages.add(32)
print('Updated Set:', numbers)

# updating set using the update() method
companies = {'Lacoste', 'Ralph Lauren'}
tech_companies = ['apple', 'google', 'apple']
companies.update(tech_companies)
print(companies)
# output: {'google', 'apple', 'Lacoste', 'Ralph Lauren'}

# Remove an element from a set using discard()
languages = {'Swift', 'Java', 'Python'}
print('Initial Set:', languages)

#romve 'Java' form the set
removedValue = languages.discard('Java')
print('Set after discard():', languages)

# Iterate Over a Set in Python
fruits = {"Apple", "Peach", "Mango"}
#for loop to access each fruits
for fruit in fruits:
    print(fruit)


# Find Number of Set Elements
#this can be dode using the len() method
even_numbers = {2, 4, 6, 8}
print('Set:', even_numbers)

# find no. of elements
print('Total Elementa:', len(even_numbers))

# PYTHON SET OPERATIONS

#1. Union of Two Sets
# the union of 2 sets A and B include all elements fo set A and B
# we use the | operator or the union() method to do set union operation

# first set
A = {1, 3, 5}
# second set
B = {0, 2, 4}
#perform union operation using |
print('Union Using |:', A | B)
#perform union operation using union()
print('Union using union():', A.union(B))

#2. Set intersection
# The intersection of 2 sets A and B include the common elements between set A and B

A = {1, 3, 5}
#second set
B = {1, 2, 3}
# perform intersection operation using &
print('Intersection using &:', A & B)
# perform intersection using intersection()
print('Intersection using intersection():', A.intersection(B))

# 3. Difference between Two Sets
# the difference btwn set A and B include elements of set A
# that are not present on set B

A = {2, 3, 5}
# second set
B = {1, 2, 6}
#perform difference operation using -
print('Difference using -:', A - B)
#perform difference operation using difference()
print('Difference using difference():', A.difference(B))

#3. Set Symmetric Difference
# the symmetric difference btwn 2 sets A and B includes all elements of A and B without the common elements
A = {2, 3, 5}
B = {1, 2, 6} # second set
# perform symmetric_difference using ^
print('Using ^:', A ^ B)
# using symmetric_difference()
print('Using symmetric_difference():', A.symmetric_difference(B))

# Check if Two Sets are equal or not
A = {1, 3, 5} #first set
B = {3, 5, 1} #second set
#perfom difference operation using ==
if A == B:
    print('Set A and Set B are equal')
else:
    print('Set A and Set B are not equal')
