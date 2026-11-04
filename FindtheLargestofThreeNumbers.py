#Accept three numbers from the user and find the largest number using if-elif-else.
a=int(input("Enter the Number for a:"))
b=int(input("Enter the Number for b:"))
c=int(input("Enter the Number for c:"))
if a>b and a>c:
    print("The Largest Number is ",a)
elif b>a and b>c:
    print("The Largest Number is ",b)
else:
    print("The Largest Number is ",c)