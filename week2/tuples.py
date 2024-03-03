#TUPLES- are similar to lists but are immutable
 #Create a Python Tuple with one element
var1 = ("Hello")
print(type(var1)) # <class 'str'>

# Creating a tuple having one element
var2 = ("hello",)
print(type(var2)) # <class 'tuple'>

#parentheis is optional
var3 = "hello",
print(type(var3)) # <class 'tuple'>

# PYTHON TUPLE METHODS
#some examples of python methods
my_tuple = ('a', 'p', 'l', 'e',)
print(my_tuple.count('p')) #prints 2
print(my_tuple.index('l')) # prints 3