speed = int(input("Enter the speed :"))

if speed >= 0 and speed <= 60:
    print(f"U are driving safe")
elif speed > 60 and speed <= 80:
    print(f"Warning.......")
elif speed > 81 and speed <= 100:
    print(f"U Have Fine 500 .......")
elif speed > 101 and speed <=120:
    print(f"U Have Fine 2000 .......")
else:
    print(f"Licence is suspended due to over speed")


   