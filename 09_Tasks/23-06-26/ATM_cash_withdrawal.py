balance = float(input("Enter the balance :"))
withdraw = float(input("Enter the withdrawal balance :"))

if balance <= 0:
    print(f"invalid Account")
elif balance == 0:
    print(f"Account Empty")
elif withdraw > balance:
    print(f"Insufficient Balance")
elif withdraw == balance:
    print(f"Account will become empty")
else:
    print(f"Transaction Successful")