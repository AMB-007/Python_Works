n = int(input("Enter N :"))
square = n ** 2
count = 0
for i in str(n):
    count += 1
print("Automorphic" if square % (10 ** count) == n else "not automorphic")
