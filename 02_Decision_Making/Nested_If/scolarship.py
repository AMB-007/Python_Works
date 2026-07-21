mark = int(input("Enter the mark :"))
income = int(input ("Enter  the income :"))

if mark >= 80:
    if income <= 20000:
        print(f"The student is eligible for  Full  Scolarship")
    else:
        print(f"the student is eligible for partial scolar ship")
elif mark >= 60 and mark <= 79:
    if income <= 100000:
        print(f"The student is eligible for partial scolarship")
    else:
        print(f"No scolarship")
else:
    print(f"No scolarship")
