numbers= [5,4,5,6,2,8,7,6,9,1]
smallest = numbers[0]
for i in numbers:
    if i < smallest:
        smallest = i
print(smallest)