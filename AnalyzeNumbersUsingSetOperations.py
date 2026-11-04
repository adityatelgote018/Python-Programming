 #Take a list of integers and divide the numbers into two sets: even numbers and odd
#numbers. Find the common elements between the two sets and verify whether the sets
#are disjoint.
a = [10, 15, 20, 25, 30, 35, 40]
even = set()
odd = set()
for x in a:
    if x % 2 == 0:
        even.add(x)
    else:
        odd.add(x)
print("List :", a)
print("Even Numbers :", even)
print("Odd Numbers :", odd)
print("\nCommon Elements :", even & odd)
print("Are sets disjoint? :", even.isdisjoint(odd))