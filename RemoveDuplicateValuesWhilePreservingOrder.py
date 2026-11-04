#Take a list containing duplicate elements. Remove duplicate elements without changing
#the original order of the elements.
a = [10, 20, 10, 30, 20, 40, 30, 50]

print("Original List :", a)

b = []

for x in a:
    if x not in b:
        b.append(x)

print("List after removing duplicates:")
print(b)