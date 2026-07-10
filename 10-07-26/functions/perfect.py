# define a function to check a number is perfect ot not using return statement
def perfect(n):
    total = 0
    for i in range(1, n//2 + 1):
        if n % i == 0:
            total += i
    return "perfect" if total == n else "not perfect"

print(perfect(6))







