num = 1634


temp = num
length = len(str(num))
sum = 0
while num > 0:
    digit = num % 10
    sum += digit ** length
    num //= 10
print("armstrong " if temp == sum else "not armstrong")