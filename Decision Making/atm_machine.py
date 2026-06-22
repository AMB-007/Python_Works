balance = 10000
min_balance = 1000


print(f"1)check balance\n2)Deposit Money\n3)Withdraw Amount\n4)Exit")
choice = input("Enter the choice :")

if choice == "1":
    print(f"Yout avaliable balance is : {balance}")
elif choice == "2":
    deposit_amount = int(input("Enter the deposit amount :"))
    balance += deposit_amount
    print(f"Your avaliable balance is :{balance}")


elif choice == "3":
    withdraw_amount = int(input("Enter the withdrawal amount : "))

    if balance >= withdraw_amount:
        print(f"You can withdraw amount{withdraw_amount}")
        
    elif balance == withdraw_amount:
        print(f"in sufficient balance{withdraw_amount}")
        if balance >= min_balance:

       
            balance - withdraw_amount
            print(f"The balance amount is {balance}")    
        

    elif min_balance >= balance:
        print(f"Cant withdraw the money minmum balance 1000 is needed{min_balance}")



elif choice == "4":
    print(f"You can exit")
       
else:
    print(f"can't do any thing Sorry")