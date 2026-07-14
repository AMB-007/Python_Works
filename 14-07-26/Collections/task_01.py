# numbers = []
# n = int(input("Enter N "))
# for i in range(1,n+1):
#     numbers.append(i)
# print(numbers)


# numbers = [1,2,3,4,5]
# for i in range(3):
#     numbers.insert(0,numbers.pop())
# print(numbers)


# numbers = [1,2,3,4,5]
# count = 0
# for i in numbers:
#     count += 1
# print(i)



numbers = [1,2,3,4,5,6,7,8,9,10]
total = 0
for i in numbers:
    if i %2 != 0:
        total += i
print(total)

