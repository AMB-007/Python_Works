total = 0
for i in range(5):
    n = int(input("Enter the number"))
    include = input("number want or not...(y)(n)")
    if include == "y":
        total += n
print(total)
