#Accept a number from the user and display its multiplication table from 1 to 10 using a for loop.
n=int(input("Enter a number: "))
print("-----------Multiplication Table-----------")
for i in range(1, 11):
    print(n ,"x" , i ,"=" , n*i)
print("------------------------------------------")
