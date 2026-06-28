n = int(input("Enter the number :"))

product = 1
while n > 0:
    digit = n % 10
    if digit  %2 != 0:
        product *= digit
    n = n // 10
print("The product of non-zero digits in the number is:", product)