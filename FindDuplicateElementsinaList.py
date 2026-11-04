#Take a list of integers and identify all elements that occur more than once. Display each
#duplicate element along with its frequency.
a = [10, 20, 10, 30, 20, 40, 10, 30, 50]

print("List :", a)
print("Duplicate Elements:")

b = []

for x in a:
    if a.count(x) > 1 and x not in b:
        print(x, ":", a.count(x), "times")
        b.append(x)