#Find the product of digits of a number.Sample Input: N = 234

n = 234
product = 1
for i in str(n):
    product *= int(i)
print(product)
