# Level 1: Basic (for loop)
# 1. Print numbers from 1 to 10.

# for i in range(1,10):
#     print(i)



# 2. Print numbers from 10 to 1.
# for i in range(10,1,-1):
#     print(i)

# 3. Print all even numbers from 1 to 50.
# for i in range(1,50):
#     if i %2 == 0:
#         print(i)


# 4. Print all odd numbers from 1 to 50.
# for i in range(1,50):
#     if i %2 != 0:
#         print(i)

# 5. Print the multiplication table of a given number.
# num = int(input("Enter the number"))
# for i in range(1,11):
#     print(num , "x", i, "=", num *i)

# 6. Find the sum of numbers from 1 to N.

# n = int(input("Enter N :"))
# sum = 0
# for i in range(1,n+1):
#     sum += i
#     print(sum)

# 7. Find the factorial of a number.
# n = int(input("Enter N :"))
# fact = 1
# for i in range(1,n+1):
#     fact *= i
#     print(fact)


# 8.Count how many numbers are divisible by 3 between 1 and N.
# n = int(input("Enter N :"))
# count = 0
# for i in range(1,n+1):
#     if i %3 == 0:
#         count += 1
# print(count)

# 9.Print the square of numbers from 1 to N.
# n = int(input("Enter N :"))
# square = 1
# for i in range(1,n+1):
#     print(i*i)

# 10.Print the cube of numbers from 1 to N.
# n = int(input("Enter N :"))
# for i in range(1,n+1):
#     print(i*i*i)


# Level 2: Number Logic (for loop)


# 1. Find the sum of all even numbers between 1 and N.
# n = int(input("Enter n :"))
# sum = 0
# for i in range(1,n+1):
#     if i %2 == 0:
#         sum += i
# print(sum)


# 2. Find the sum of all odd numbers between 1 and N.

# n = int(input("Enter N :"))
# sum = 0
# for i in range(1,n+1):
#     if i %2 != 0:
#         sum += i
# print(sum)


# 3 . Count the digits in a number.
# n = int(input("Enter n :"))
# count = 0
# while n > 0:
#     n //= 10
#     count += 1
# print(count)


# 4 .Reverse a number.
# n = int(input("Enter N :"))
# reverse = 0
# while n > 0:
#     digit = n % 10
#     reverse = reverse * 10 + digit
#     n //= 10
# print(reverse)


# 5.Check whether a number is a palindrome.
# n = int(input("Enter n :"))
# orginal = n
# reverse = 0
# while n > 0:
#     digit = n % 10
#     reverse = reverse * 10 + digit
#     n //= 10
# if orginal == reverse:
#     print("palindrome")
# else:
#     print("not palindrome")


# 6. Find the largest digit in a number.
# n = int(input("Enter a number :"))
# largest = 0
# while n > 0:
#     digit = n % 10
#     if digit > largest:
#         largest = digit
#     n //= 10
# print(largest)


# 7. Find the smallest digit in a number.
# n = int(input("Enter a number :"))
# smallest = 9
# while n > 0:
#     digit = n % 10
#     if digit < smallest:
#         smallest = digit
#     n //= 10
# print(smallest)


# 8. Find the sum of digits.

# n = int(input("Enter a number :"))
# sum = 0
# while n > 0:
#     digit = n % 10
#     sum += digit
#     n //= 10
# print(sum)

# 9. Find the product of digits.
# n = int(input("Enter a number :"))
# product = 1
# while n > 0:
#     digit = n % 10
#     product *= digit
#     n //= 10
# print(product)

# 10. Print every digit separately.
# n = int(input("Enter a number :"))
# while n > 0:
#     digit = n % 10
#     print(digit)
#     n //= 10


# Level 3: Prime Numbers

# 1. Check whether a number is prime.
# n = int(input("Enter a number :"))
# count = 0
# for i in range(1,n+1):
#     if n % i == 0:
#         count += 1
# if count == 2:
#     print("prime")
# else:
#     print("not prime")


# 2. Print all prime numbers from 1 to N.
# n = int(input("Enter N: "))
# for i in range(2, n + 1):
#     count = 0
#     for j in range(1, i + 1):
#         if i % j == 0:
#             count += 1
#     if count == 2:
#         print(i)




# 3. Count the number of primes from 1 to N.
n = int(input("Enter N: "))

prime_count = 0
for i in range(2, n + 1):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
    if count == 2:
        prime_count += 1
print("Number of prime numbers =", prime_count)








