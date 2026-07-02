# Nearest Prime Number

# Task:
# Given a number N, print the first prime number greater than N.

N = 20
n = 20
for i in range(n+1,100):
    count = 0
    for j in range(1,i+1):
        if i % j == 0: 
            count += 1
    if count == 2:
        print(i) 
        break   




