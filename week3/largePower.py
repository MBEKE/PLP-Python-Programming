# define function
def large_power(base, exponent):
    # calculate result of base to the power of exponent
    result = base ** exponent
    # check for the result value in relation to 5000
    if result > 500:
        return True
    else:
        return False
# call the function
result = large_power(30, 20)
print("Is the result greatert than 500?", result)
print("End of program")