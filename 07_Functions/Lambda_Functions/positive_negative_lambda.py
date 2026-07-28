# Lambda function to check if a number is positive, negative, or zero

check_number = lambda num: "positive" if num > 0 else ("negative" if num < 0 else "zero")

print("55 is:", check_number(55))
print("-12 is:", check_number(-12))
print("0 is:", check_number(0))
