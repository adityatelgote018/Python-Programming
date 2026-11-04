#Display numbers from 1 to 20, but use the continue statement to skip odd numbers and print only even numbers.
print("------Even Numbers------")
for i in range(1, 21):
    if i % 2 !=0:
        continue
    print(i)
print("-------------------------")
