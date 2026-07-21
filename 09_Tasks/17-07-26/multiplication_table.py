# Q3. Print the multiplication table of a number
# Input: 7

n = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
