# Q4. Find the sum of all even numbers between two given numbers
# Input: 10 20   Output: 90

start = int(input("Enter start number: "))
end   = int(input("Enter end number: "))
total = 0

for i in range(start, end + 1):
    if i % 2 == 0:
        total += i

print("Sum of even numbers:", total)
