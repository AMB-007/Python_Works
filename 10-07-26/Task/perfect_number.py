def perfect_number(num):

    total = 0

    for i in range(1, num):
        if num % i == 0:
            total += i

    if total == num:
        return "Perfect Number"
    else:
        return "Not Perfect Number"


num = int(input("Enter a number: "))

print(perfect_number(num))