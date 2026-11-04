 #Take a list of numbers and use a dictionary to calculate the frequency of every element.
#Display the element with the highest frequency.
a = [10, 20, 10, 30, 20, 10, 40, 20, 10]
frequency = {}
for x in a:
    if x in frequency:
        frequency[x] += 1
    else:
        frequency[x] = 1
print("List :", a)
print("Frequency:")
for x in frequency:
    print(x, ":", frequency[x])
most = max(frequency, key=frequency.get)
print("Most Frequent Element :", most)
print("Frequency :", frequency[most])