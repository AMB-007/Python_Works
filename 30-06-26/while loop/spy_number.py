n = int(input("Enter N :"))
sum = 0
product = 1

while(n > 0):
    digit = n % 10
    sum += digit
    product*= digit
    n //= 10
print(product)
print(sum)
print("Spy number" if sum == product else "not spy number")