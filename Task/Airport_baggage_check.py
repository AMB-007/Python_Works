weight = int(input("Enter the weight :"))

if weight == 0:
    print(f"Invalid Weight")
elif weight >= 1 and weight <= 15:
    print(f"Allowed")
elif weight >= 16 and weight <= 25:
    print(f"Extra Charge")
elif weight >= 26 and weight <= 40:
    print(f"Heavy Baggage")
else:
    print(f"Not Allowed")