# if - Statement
discount = 0
amount = 1200

# check the ammount value
if amount > 1000:
    discount = amount * 10 / 100

print("Amount = ", amount - discount);

# if-else - statements
age = 25
print("age: ", age)
if age >= 18:
    print('Eligible to vote')
else:
    print('not eligible to vote')

#if elif else - statements
amount = 2500
print('Amount = ',amount)
if amount > 10000:
    discount = amount * 20 / 100
elif amount > 5000:
    discount = amount * 10 / 100
elif amount > 1000:
    discount = amount * 5 / 100
    
else:
    discount = 0

print('Payable amount = ',amount - discount)

# Nested if-else statements
num = 8
print("num = ", num)
if num % 2 == 0:
    if num % 3 == 0:
        print('Divisible by 3 and 2')
    else:
        print('Divisibe by 2 not divisible by3')
else:
    if num % 3 == 0:
        print('Divisible by 3 not divisible by 2')
    else:
        print('not Divisible by 2 not divisible by 3')


