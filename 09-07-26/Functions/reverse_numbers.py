
def reverse_number(num_1):
    rev = 0
    while num_1 > 0:
        digit = num_1 % 10
        rev = rev * 10 + digit
        num_1 //= 10
    print(rev)
reverse_number(95)