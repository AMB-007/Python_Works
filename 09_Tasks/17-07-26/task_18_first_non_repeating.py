# Q18. Find the first non-repeating element in a list
# Input: [2,3,4,2,3,5,6]   Output: 4

numbers = [2, 3, 4, 2, 3, 5, 6]
result  = None

for num in numbers:
    count = 0
    for n in numbers:
        if n == num:
            count += 1
    if count == 1:
        result = num
        break

if result is not None:
    print("First non-repeating element:", result)
else:
    print("No non-repeating element found")
