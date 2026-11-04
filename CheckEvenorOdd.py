#Accept an integer from the user and check whether the number is even or odd using the modulus operator and conditional statement.
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(num, "is an Even Number.")
else:
    print(num, "is an Odd Number.")
