data = int(input("Enter the data :"))

if data == 0:
    print(f"No Usage")
elif data >= 1 and data <= 2:
    print(f"Normal Usage")
elif data >=3 and data <= 5:
    print(f"High Usage")
elif data >= 6 and data <= 8:
    print(f"Warning")
else:
    print("Limit Exceeded")