n = int(input("Enter the number: "))

largest_even = -1

while n > 0:
    digit = n % 10

    if digit % 2 == 0 and digit > largest_even:
        largest_even = digit

    n = n // 10

if largest_even == -1:
    print("No even digit found")
else:
    print("Largest even digit:", largest_even)