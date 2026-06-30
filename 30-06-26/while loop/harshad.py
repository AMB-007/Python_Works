n = int(input("Enter N :"))
temp = n
sum = 0

while n > 0:
    digit = n % 10
    sum += digit
    n //= 10
print("harshad" if temp % sum == 0 else "not harshad")
