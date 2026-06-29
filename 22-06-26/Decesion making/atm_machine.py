balance = 10000
min_balance = 1000

print(f"1)check balance\n2)Deposit Money\n3)Withdraw Amount\n4)Exit")
choice = input("Enter the choice :")

if choice == "1":
    print(f"The balance is :{balance}")

elif choice == "2":
    deposit_amount = int(input("Enter the deposit amount :"))
    balance += deposit_amount
    print(f"The deposied amount is : {deposit_amount}and the updated balance is :{balance}")

elif choice =="3":
    withdraw = int(input("Enter the withdrawal amount :"))
    if withdraw > balance:
        print(f"Insufficient Balance")
    elif balance - withdraw < min_balance:
        print(f"Minimum Balance of{min_balance} must be maintained Your balance is {balance}")
    else:
        balance -= withdraw
        print(f"The withdrawal successful\nAvaliable balance is{balance}")
        
elif choice == "4":
    print(f"THANK YOU FOR USING THE ATM")
else:
    print(f"Invalid Choice Please choose Correct Option")
