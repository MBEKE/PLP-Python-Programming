# Funtion - a modular piece of code that can be used repeatedly

# Creating a Function
def add_nums():
    print( 2 + 13)

# Calling a Funtion
add_nums() # Output => 13

# Function Arguments/ Parameters
def add_nums(a, b):
    answer = a + b
    return answer
# assign function call to a variable called total
total = add_nums(2, 13)
print("Total : ", total)

# Arbitrary Argument, *args
# If you don't know how many arguments that wil be passed into your function add a *berof e the param name
def add_nums(*nums):
    sum = 0
    for num in nums:
        sum += num
    return sum
print("Total: ", add_nums(2, 5, 6, 7, 8, 13))

# Arbitrary Keyword Arguments, **kwargs
# if the number of kwargs is unknown, add a ** befor the parameter name:
def add_ages(**ages):
    sum = 0
    for k, v in ages. items():
        sum += v
        return sum
print("Total: ", add_ages(mutemi = 123, skinny = 22, ahmed = 21))
