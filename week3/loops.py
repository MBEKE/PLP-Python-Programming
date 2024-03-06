# while loop - repeatedly executes a target statement as long as a given boolean expression is true

# example 1:
count = 0
while count < 5:
    count += 1
    print("Iteration no. {}".format(count))
print("End of while loop")

# example 2:
var = '0'
while var.isnumeric() == True:
    var = input("enter a number: ")
    if var.isnumeric() == True:
        print("Your input", var)
print(("End of while loop"))

# while-else loop:
# example
count = 0
while count < 5:
    count += 1
    print("Iteration no. {}".format(count))
else:
    print("While loop over. Now in else block")
print("End of while loop")