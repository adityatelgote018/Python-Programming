#Accept a number from the user and check whether it is prime or not. Use break to stop the loop when a divisor is found.
n=int(input("Enter the Number:"))
for i in range(2,n):
    if n%i==0:
        print(n, "is not a prime number")
        break
else:
        print(n, "is a prime number")
