def armstrong(n):
    temp = n
    total = 0
    digits = len(str(n))

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp = temp // 10

    if total == n:
        print("Armstrong")
    else:
        print("Not Armstrong")

armstrong(153)