hours = float(input("Enter the Hours :"))

if hours == 0:
    print(f"Invalid Hours")

elif hours >= 1 and hours <= 2:
    print(f"Parking fee is 20")

elif hours >= 3 and hours <= 5:
    print(f"Parking fees is 50")

elif hours >= 6 and hours <= 10:
    print(f"Parking fees is 100")

else:
    print(f"Invalid Hours")

