'''
Lambda function - a function without a name. Also called anonymus function
Are efficient in creating a function that will contain only simple expressions
Also useful creating one time use functions
For declaration, use 'lambda' keyword in place of 'def'
'''
# Example
snack = lambda : print("Njugu")

# calling the lambda
snack() # Output: Njugu

# Lambda function with arguments
num_square = lambda num: num **2

# calling the lambda insine print()
print("Square of num is: ", num_square(8))
