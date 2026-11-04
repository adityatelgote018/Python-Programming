#Take a list of integers containing duplicate values and find the largest and second-
#largest distinct elements without using the sort() function.
a = [45, 20, 67, 67, 35, 90, 45, 80]
largest = None
second = None
for x in a:
    if largest is None or x > largest:
        second = largest
        largest = x
    elif x != largest and (second is None or x > second):
        second = x
print("List :", a)
print("Largest Element :", largest)
print("Second Largest Element :", second)