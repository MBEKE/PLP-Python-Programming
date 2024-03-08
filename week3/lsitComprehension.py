# say we have a list of integers and wanted to create a list where each element is doubled
# without comprehesion
nums = [4, -11, 69, 53, -65]
doubled = []

for num in nums:
    doubled.append(num * 2)

print(doubled)

# Using List Comprehenison
doubled = [num * 2 for num in nums]
print(doubled)