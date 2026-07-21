# definea function to check and return the armstrong numbers from 100 to 1000
def armstrong():
    result = ""

    for n in range(100, 1001):
        temp = n
        total = 0

        while temp > 0:
            digit = temp % 10
            total = total + digit ** 3
            temp = temp // 10

        if total == n:
            result = result + str(n) + " "

    return result

print(armstrong())

