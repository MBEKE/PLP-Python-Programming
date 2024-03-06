# for loop - iterate over the items of any sequence e.g list,tuple

# for Loop with Strings
zen = '''
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
'''

for char in zen:
    if char not in 'aeiou':
        print(char, end='')

# for Loop with Tuples
numbers = (34,54,67,21,78,97,45,44,80,19)
total = 0
for num in numbers:
    total += num
print("Total =", total)


#for Loop with Lists
numbers = [34,54,67,21,78,97,45,44,80,19]
total = 0
for num in numbers:
    if num % 2 == 0:
        print(num)

# for Loop with Range Objects
numbers = range(5)
'''
start is 0 by default,
step is 1 by default,
range generated from 0 to 4
'''
print(list(numbers))
# step is 1 by default, range generated from 10 to 19
numbers = range(10,20)
print(list(numbers))
# range generaterd from 1 to 10 increment by step of 2
numbers = range(1, 10, 2)
print(list(numbers))

for num in range(5):
    print(num, end=' ')
print()
for num in range(10, 20):
    print(num, end=' ')
print()
for num in range(1, 10, 2):
    print(num, end=' ')

# for loop with Sequence Indixes
numbers = [34,54,67,21,78]
indices = range(len(numbers))
for index in indices:
    print("Index:", index, "number:",numbers[index])

# for Loop with dictioneries
numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
for x in numbers:
    print(x)

# for-else Loop in Python
    for count in range(6):
        print("Iteration no. {}".format(count))
    else:
        print('for loop over. Now in else block')
    print("End of for loop")

# Nested for Loop
for i in range(1, 11):
    for j in range(1,11):
        k = i * j
        print("{:3d}".format(k), end=' ')
print()
