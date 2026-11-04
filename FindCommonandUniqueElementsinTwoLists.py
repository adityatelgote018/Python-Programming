#Take two lists of integers from the user. Convert them into sets and find the common
#elements, elements present only in the first list, elements present only in the second list,
#and all unique elements.

a = []
n = int(input("Enter number of elements in first list: "))
for i in range(n):
    x = int(input("Enter element: "))
    a.append(x)
# Second list
b = []
n = int(input("Enter number of elements in second list: "))
for i in range(n):
    x = int(input("Enter element: "))
    b.append(x)
# Convert into sets
a = set(a)
b = set(b)
# Display results
print("Common Elements :", a & b)
print("Only in First List :", a - b)
print("Only in Second List :", b - a)
print("All Unique Elements :", a | b)