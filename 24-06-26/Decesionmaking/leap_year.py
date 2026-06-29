year = int(input("Enter the year :"))
if year %4 == 0 and year %400 ==0 or year %100 != 0:
    print("Its Leap Year")
else:
    print("Its not Leap Year")

#print(f"Its Leap Year" if year %4 == 0 and year %400 ==0 or year %100 != 0 else "Its not Leap Year")
