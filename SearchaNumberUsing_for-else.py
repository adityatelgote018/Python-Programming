#Accept a number from the user and search for it in the numbers from 1 to 10. If the number is found, use break. If the loop completes without finding the number, execute the else block.
n=int(input("Enter the number to search :"))
for i in range(1, 11):
    if i==n:
        print("Number" ,n ,"is Found")
        break
else:
    print("Number" ,n ,"is Not Found")
