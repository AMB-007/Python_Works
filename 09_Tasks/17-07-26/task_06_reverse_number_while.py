# Q6. Find the reverse of a number using while loop
# Input: 12345   Output: 54321

n   = int(input("Enter a number: "))
rev = 0

while n > 0:
    digit = n % 10
    rev   = rev * 10 + digit
    n     = n // 10

print("Reversed number:", rev)
