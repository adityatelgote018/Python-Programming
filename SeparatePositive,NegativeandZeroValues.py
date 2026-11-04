#Take a list of integers and create three separate lists containing positive numbers,
#negative numbers, and zeros.
a = [10, -5, 0, 20, -15, 0, 30, -2]
positive = []
negative = []
zeros = []
for x in a:
    if x > 0:
        positive.append(x)
    elif x < 0:
        negative.append(x)
    else:
        zeros.append(x)
print("Original List :", a)
print("Positive Numbers :", positive)
print("Negative Numbers :", negative)
print("Zeros :", zeros) == [10, -5, 0, 20, -15, 0, 30, -2]
positive = []
negative = []
zeros = []
for x in a:
    if x > 0:
        positive.append(x)
    elif x < 0:
        negative.append(x)
    else:
        zeros.append(x)
print("Original List :", a)
print("Positive Numbers :", positive)
print("Negative Numbers :", negative)
print("Zeros :", zeros)