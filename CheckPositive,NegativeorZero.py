#Accept a number from the user and determine whether it is positive, negative, or zero.
a=int(input("Enter the Number:"))
if a>0:
    print(a ,"is Positive Number.")
elif a<0:
    print(a ,"is Negative Number.")
else:
    print(a ,"is Zero Number.")