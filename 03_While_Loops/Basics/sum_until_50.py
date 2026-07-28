# Question: Write a Python program using while loop to repeatedly accept numbers until total sum reaches 50.

total = 0
while total <= 50:
    number = int(input("Enter the number :"))
    total += number
print(f"The total is : {total}")
