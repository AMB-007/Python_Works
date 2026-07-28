# Question: Write a Python program using for loop to selectively sum 5 user-input numbers based on confirmation.

total = 0
for i in range(5):
    n = int(input("Enter the number"))
    include = input("number want or not...(y)(n)")
    if include == "y":
        total += n
print(total)

