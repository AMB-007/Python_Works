days = int(input("Enter the Days: "))
years = days // 365
remaining_days = days % 365
months = remaining_days // 30
days_left = remaining_days % 30


print(f"Year is:{years}\nMonths are:{months}\nRemaining days are:{days_left}")
