n = int(input("Enter the number :"))
i = 1
even_sum = 0
even_odd = 0
while(i <= n):
    if i %2 == 0 :
        even_sum += i
    else:
        even_odd += i
    i += 1
difference = even_sum - even_odd
print(difference)
print(even_sum)
print(even_odd)




