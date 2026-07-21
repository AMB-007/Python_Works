def prime(n):

    if n <= 1:
        return "Not Prime Number"

    for i in range(2, n):
        if n % i == 0:
            return "Not Prime Number"

    return "Prime Number"


num = int(input("Enter a number: "))

print(prime(num))