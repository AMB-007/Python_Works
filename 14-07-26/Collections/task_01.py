# numbers = []
# n = int(input("Enter N "))
# for i in range(1,n+1):
#     numbers.append(i)
# print(numbers)


numbers = [1,2,3,4,5]
for i in range(3):
    numbers.insert(0,numbers.pop())
print(numbers)



