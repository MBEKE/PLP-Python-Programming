# LISTS - they are mutable
# empty list
my_list = []
#list with mixed data types
my_list = [1, "Hello", 3.4] #int, str, float

#ACCESS PYTHON LIST ELEMENTS
languages =["Python", "Swift", "C++"]
#access item at index 0
print(languages[0]) #python
#access item at index 2
print(languages[2]) #C++
#accessing the last item on the list
print(languages[-1])

#SLCING OF A PYTHON LIST
letter_list = ['p','r','o','g','r','a','m','i']
#items form index 2 to index 4
print(letter_list[2:5]) #Output: ['o','g','r']
#items from index 5 to end
print(letter_list[5:])
#items beginning to end
print(letter_list[:])
#access item at index 2
print(languages[-3])

#ADDING ELEMENTS TO A PYTHON LIST
#1. Using append()
numbers = [21, 34, 54, 12]
print("Before Append:", numbers)
#using append method
numbers.append(32)
print("After Append:", numbers)

#2. Using extend()
prime_numbers = [2, 3, 5]
print("List1:",prime_numbers)

even_numbers = [4, 6, 8]
print("List2:", even_numbers)
#join the two lists
prime_numbers.extend(even_numbers)

#CHANGE LIST ITEMS
fruits = ["Mango", "Apple", "Orange", "Pineapple"]
#changing the 3rd item to Banana
fruits[2] = "Banana"
print(fruits)#["Mango", "Apple", "Banana", "Pinaeapple"]

#REMOVE AN ITEM FROM A LIST
#1. Using del()
students =["John", "Rose", "Joseph", "Lynn", "Mary", "Rodgers"]
#deleting the second item
del students[1]
print(students)

#deleting the last item
del students[-1]
print(students)

#deleting the first two items
del students[0 : 2]
print(students)

#2. Using remove()
subjects = ["Eng", "Kis", "Mat", "Geog", "Hist"]
#remove "Mat" from the list
subjects.remove("Mat")
print(subjects)

# ITERATING THROUGH A LIST
food = ["Rice", "Beef", "Fish", "Chapati", "Chicken"]
#iterating through the list
for food in food:
    print(food)

# PYTHON LIST COMPREHENSION
    # this is a concise and elegant way to create lists
numbers = [number*number for number in range(1,6)]
print(numbers)
#Output: [1, 4, 9, 16, 25]