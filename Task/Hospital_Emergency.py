priority = int(input("Enter the a button for a treatment:"))

if priority == 0:
    print(f"no Treatment Required")

elif priority >= 1 and priority <=3:
    print(f"Need normal Checkup")

elif priority >= 4 and priority <= 6:
    print(f"Priority checkup")

elif priority <= 7 and priority <= 8:
    print(f"Emergency Ward")

elif priority >= 9 and priority <= 10:
    print(f"ICU admission")

else:
    print(f"Invalid priority")