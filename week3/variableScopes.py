# 1. LOCAL SCOPE
# Refers to a variable declared inside a function
# Example..
def add_nums(a, b):
    #local variable  declared inside a function
    answer = a + b
    return answer
# Calling our function inside print statement
print(add_nums(2, 13))

#2. ENCLOSING SCOPE
# refers to a function inside another function (nested function)
# Example ..
def add_number(a, b):
    #enclosed variable declared inside a function
    answer1 = a + b
    def double_it():
        #local variable
        double1 = answer * 2
        print(double1)
    double_it() # calling inner funciton
    return answer1
# Calling function inside print statement
print(add_number(2, 13))

# Global Scope
# a variable is declared outside a function and can be accessed everywhere
# #Example..
global_var = 13
def add_number(a, b):
    #enclosed variable declared inside a function
    answer1 = a + 
    print("Global_var in outer function: ", global_var)
    def double_it():
        #local variable
        double1 = answer * 2
        print("Global_var in outer function: ", global_var)
        print(double1)
    double_it() # calling inner funciton
    return answer1
# Calling function inside print statement
print(add_number(2, 13))

#4. BUILT-IN SCOPE
# Refers to the reserved keywords that python uses for its buit-in functions, eg print def, for, in