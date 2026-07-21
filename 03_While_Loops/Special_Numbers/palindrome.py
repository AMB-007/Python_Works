num = int(input("Enter N :"))

temp = num
reversed = 0
while num > 0:
    digit = num % 10
    reversed  = reversed * 10 + digit
    num //= 10
print("palindrome"if temp == reversed else "not palindrome")