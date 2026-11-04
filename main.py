import Bank

print("\n----Bank System----")
print("1.Deposite.")
print("2.Withdraw.")
print("3.Check Balance.")
print("4.Exit.")
while True:
    choice=int(input("Enter Your Choice(1-4) :"))
    if choice==1:
        amount=float(input("Enter Amount to Deposit :"))
        Bank.deposit(amount)
        print("-------------------------")
    elif choice==2:
        amount=float(input("Enter Amount to Withdraw :"))
        Bank.withdraw(amount)
        print("---------------------------")
    elif choice==3:
        Bank.check_balance(amount)
        print("---------------------------")
    elif choice==4:
        print("Thank You for using this Bank System")
        break
    else:
        print("Invalid Choice!")
