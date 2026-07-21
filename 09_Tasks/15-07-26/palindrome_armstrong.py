#  Find Palindrome and Armstrong Numbers
# Sample Input: [121,153,123,370,454,407,99]


numbers = [121, 153, 123, 370, 454, 407, 99]

palindrome = []
armstrong = []

for num in numbers:


    temp = num
    reverse = 0

    while temp > 0:
        digit = temp % 10
        reverse = reverse * 10 + digit
        temp = temp // 10

    if reverse == num:
        palindrome.append(num)

   
    temp = num
    digits = len(str(num))
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp = temp // 10

    if total == num:
        armstrong.append(num)

print(palindrome)
print(armstrong)