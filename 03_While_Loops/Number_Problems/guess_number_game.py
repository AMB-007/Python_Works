# Question: Write a Python program simulating a number guessing game with 'Too High' and 'Too Low' hints using while loop.

num = 50
n = int(input("Enter the number :"))
count = 1
while  n != num:
    print("Too Low" if n< num else "Too High")
    n = int(input("Enter the number :"))
    count += 1
print(f"congrats u took {count} attempts")

