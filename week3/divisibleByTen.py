def divisible_by_ten(num):
    result = num % 10
    if result == 0:
        return True
    else: 
        return False
    
# function calling
print(divisible_by_ten(45))