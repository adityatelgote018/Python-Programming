#Problem Statement: Swap two numbers using temporary and without temporary variable.

a = 10
b = 20

print("Before Swapping: a=10 b=20")

# Using temporary variable
temp = a
a = b
b = temp

print("After Swapping: a=20 b=10")

# Without temporary variable
a, b = b, a