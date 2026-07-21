# Q9. Find the largest digit in a number
# Input: 294816   Output: 9

n       = int(input("Enter a number: "))
largest = 0

while n > 0:
    digit = n % 10
    if digit > largest:
        largest = digit
    n = n // 10

print("Largest digit:", largest)
