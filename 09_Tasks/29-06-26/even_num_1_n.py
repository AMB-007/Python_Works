#Print all even numbers from 1 to N.Sample Input: N = 20

n = int(input("Enter N :"))


for i in range ( 1, n + 1):
    if i %2 == 0:
        print(i)

