balance=0

def deposit(amount):
    global balance
    balance+=amount
    print("Amount deposited successfully.")
    print("Current Balance : ",balance)
def withdraw(amount):
    global balance
    if amount<=balance:
        balance-=amount
        print("Amount withdrawn successfully.")
        print("Current Balance : ",balance)
    else:
        print("Insufficient balance.")

def check_balance(amount):
    print("Current Balance : ",balance)
    