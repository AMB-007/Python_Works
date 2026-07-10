#Given an integer n, return True if n is within 10 of either 100 or 200

def integer(n):
    if (90 <= n <= 110 or 190 <= n <= 210):
        return True
    else:
        return False

print(integer(110))
print(integer(255))