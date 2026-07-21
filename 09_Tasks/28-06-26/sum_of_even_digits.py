n = int(input("Enter the number :"))

sum_even = 0
while (n > 0):
    digit = n % 10
    if digit % 2 == 0:
        sum_even += digit
    n = n // 10
print("The sum of even digits in the number is:", sum_even)
       


