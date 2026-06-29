n = int(input("Enter a number "))
i = 1
while (i <= n):
    #if ( i % 2 ==0):
    #    print(i)
    print(f"The number is even"if i %2 == 0 else "The number is odd")
    print(i)
    i = i + 1