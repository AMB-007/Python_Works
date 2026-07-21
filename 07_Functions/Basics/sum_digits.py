# define a function to return the sum of digits of the number



def sum_of_digit(num_1):
    total = 0

    while num_1 > 0:
        digit = num_1 % 10
        total = total + digit
        num_1 = num_1 // 10

    return total

num = int(input("Enter a number: "))
print("Sum of digits =", sum_of_digit(num))