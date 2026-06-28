n = int(input("Enter the number :"))
sum_even = 0
sum_odd = 0

while n > 0:
    digit = n % 10
    if digit %2 == 0:
        sum_even += digit
    else: 
        sum_odd += digit
    n = n // 10
difference = sum_even - sum_odd
print(difference)