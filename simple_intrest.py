principle = float(input("Enter the Principle Amount:"))
rate_intrest = float(input("Enter the Intrest:"))
tendure = int(input("Duration in months:"))

SI = ( principle * rate_intrest *  tendure ) / 100 
print("Simple Intrest is:",SI)