balance = 10000
atmpin = 8686
history = []
def showbalance():
    s = input("Do you want to view your balance? (YES/NO)")
    if s.lower() =='yes':
        print(f"Remaining balance : {balance}")
def deposit():
    global balance
    print("You have chose to deposit !")

    name = input("Enter the name of the person you want to deposit cash to : ")
    acc = input("Enter 12 digit account number : ")

    if len(acc) != 12 or not acc.isdigit():
        print("Invalid Account number")
        return

    cash = int(input("Enter the amount you want to transfer : "))

    if cash <= 0:
        print("Invalid amount")
    elif cash > balance :
        print("Insuffiecient funds")

    else:
        if acc == "886730010731":
            balance += cash
            print(f"You have successfully deposited {cash} to yourself")
            history.append(f"Deposited {cash}/- ")
            showbalance()
        else:
            balance -= cash
            print(f"You have successfully deposited {cash} to {name}")
            history.append(f"Transferred {cash}/- to {name}")
            showbalance()
def withdraw():
    global balance
    print("You have chosen to withdraw!")

    try :
        pin = int(input("Enter your pin : "))
    except ValueError:
        print("PIN must be number only")
        return
    i = int(input("How much cash do you wish to withdraw : "))

    if i > balance:
        print("Insufficient funds")

    elif i <= 0:
        print("Invalid Amount")

    else:
        if pin == atmpin:
            balance -= i
            print(f"You have successfully withdrawn: {i}.")
            print(f"Remaining balance : {balance}")
            history.append(f"Withdrew {i}/-")
            

        else:
            print("Invalid pin")
def checkbalance() :
    print("You have chose to Check Balance !")

    pin = int(input("Enter your pin : "))

    if pin == atmpin:
        print(f"Your current balance is : {balance}")

    else:
        print("Invalid pin")
def transactionhistory():
    if len(history) == 0:
        print("No history found")
    else:
        print("Transaction History : ")
        for i in history :
            print(i)
while True:
    print("====== ATM SYSTEM ======")
    print("What do you want to proceed with?")
    print("1.DEPOSIT")
    print("2.WITHDRAW")
    print("3.CHECK BALANCE")
    print("4.Transaction History")
    print("5.EXIT")

    a = input("Enter your choice : ")

    if a == "1":
        deposit()
    elif a == "2":
        withdraw()
    elif a == "3":
        checkbalance()
    elif a == "4":
        transactionhistory()
    elif a == "5":
        ask = input("Are you sure you want to exit?\n")
        if ask.lower() == "yes":
            break
        elif ask.lower() == "no":
            print("You will now be redirected to the MENU.")
    else:
        print("Invalid Choice, Enter (1 - 5)\n")
