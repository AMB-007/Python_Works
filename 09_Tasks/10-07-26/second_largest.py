def second_largest(a, b, c, d, e):

    numbers = [a, b, c, d, e]
    numbers.sort()

    return numbers[-2]


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))
e = int(input("Enter fifth number: "))

print("Second Largest =", second_largest(a, b, c, d, e))