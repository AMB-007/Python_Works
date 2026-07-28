# Question: Write a Python program to check whether a number is divisible by 5 and 3 using if conditions.

# Lambda function to filter numbers divisible by both 3 and 5

numbers = [10, 15, 20, 30, 45, 50, 60]
filter_divisible = lambda num_list: [i for i in num_list if i % 3 == 0 and i % 5 == 0]

print("Original list:", numbers)
print("Divisible by 3 and 5:", filter_divisible(numbers))

