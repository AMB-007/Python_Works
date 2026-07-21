mark = int(input("Enter the mark :"))

if mark == 100:
    print(f"Perfect Score")
elif mark >= 75 and mark <= 99:
    print(f"Passed with Distinction")
elif mark >=50 and mark <= 74:
    print(f"Passed")
elif mark >= 35 and mark <= 49:
    print(f"Re-appear")
else:
    print(f"Failed")