# wap to remove all the prime numbers(should be greater than 1 )from the list

numbers = [3,1,5,8,6,14,13,11]
for i in numbers.copy():
        if i > 1:
            for j in range(2,i):                    
                if i % j == 0:
                    break
            else:
                numbers.remove(i)
print(numbers)  