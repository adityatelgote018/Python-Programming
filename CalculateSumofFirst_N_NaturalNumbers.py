#Accept a positive integer N and calculate the sum of the first N natural numbers using a loop.
N = int(input("Enter N: "))
sum = 0
for i in range(1, N + 1):
    sum+=i
print("Sum of first", N, "natural numbers:  ", sum)