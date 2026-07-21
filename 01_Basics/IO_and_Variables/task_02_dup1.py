# Shift all zeros to the end

numbers = [0,0,5,0,3,8,0,2]
result = []
for i in numbers:
    if i != 0:
        result.append(i)
for i in numbers:
    if i == 0:
        result.append(i)
print(result)