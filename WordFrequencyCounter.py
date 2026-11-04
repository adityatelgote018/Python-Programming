#Take a sentence from the user and create a dictionary containing each word and its
#frequency. Ignore differences between uppercase and lowercase letters.
sentence = input("Enter a sentence : ")
words = sentence.lower().split()
frequency = {}
for word in words:
    if word in frequency:
        frequency[word] = frequency[word] + 1
    else:
        frequency[word] = 1
print("Word Frequency:")
for word in frequency:
    print(word, ":", frequency[word])