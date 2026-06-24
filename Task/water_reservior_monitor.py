level = float(input("Enter the level :"))

if level == 0:
    print(f"Reservior is Empty")
elif level >= 1 and level <=25:
    print(f"Critical Level")
elif level >= 26 and level <=50:
    print(f"Low Level")
elif level >= 51 and level <=75:
    print(f"Normal Level")
elif level >=76 and level <=100:
    print(f"Full Capacity")
else:
    print(f"Invalid Level")