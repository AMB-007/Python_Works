# ============================================================
#              🐍 PYTHON PRACTICE WORKSPACE (10 PROBLEMS)
# ============================================================
# Workspace: d:\Python_Works\Python-pratice\pratice.py
# Questions File: d:\Python_Works\Python-pratice\questions.txt
# ============================================================


# ------------------------------------------------------------
# Q1. Armstrong Number Checker (Loops & Digit Math)
# ------------------------------------------------------------
"""
Problem:
Write a program to check if a given positive integer is an Armstrong number.
An Armstrong number of n digits is equal to the sum of its digits raised to the n-th power.
(e.g., 153 has 3 digits: 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153).

Sample Input:  153
Sample Output: 153 is an Armstrong Number
"""

def is_armstrong(n):
    # TODO: Write your logic here
    pass

# Test Q1:
# print(is_armstrong(153))


# ------------------------------------------------------------
# Q2. Find Second Largest Element in a List (Collections & Logic)
# ------------------------------------------------------------
"""
Problem:
Write a function `find_second_largest(lst)` that returns the second largest 
unique number in a list WITHOUT using built-in `sort()` or `max()`.

Sample Input:  [12, 35, 1, 10, 34, 35, 1]
Sample Output: 34
"""

def find_second_largest(lst):
    # TODO: Write your logic here without using sort() or max()
    pass

# Test Q2:
# print(find_second_largest([12, 35, 1, 10, 34, 35, 1]))


# ------------------------------------------------------------
# Q3. Character Frequency Counter (Strings & Dictionaries)
# ------------------------------------------------------------
"""
Problem:
Write a program that takes a string and prints a dictionary containing the count 
of repeating characters (characters appearing more than once).

Sample Input:  "programming"
Sample Output: {'r': 2, 'g': 2, 'm': 2}
"""

def repeating_char_frequency(s):
    # TODO: Return dict of characters with count > 1
    pass

# Test Q3:
# print(repeating_char_frequency("programming"))


# ------------------------------------------------------------
# Q4. Prime Numbers in a Range (For Loop & Range)
# ------------------------------------------------------------
"""
Problem:
Write a program to find and print all prime numbers between a `start` and `end` value.

Sample Input:  start = 10, end = 30
Sample Output: [11, 13, 17, 19, 23, 29]
"""

def primes_in_range(start, end):
    # TODO: Return list of prime numbers between start and end
    prime_list = []

    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                prime_list.append(num)

    return prime_list


    pass

# Test Q4:
# print(primes_in_range(10, 30))


# ------------------------------------------------------------
# Q5. Rotate List to the Right by K Positions (List Operations)
# ------------------------------------------------------------
"""
Problem:
Given a list of numbers `lst` and an integer `k`, rotate the list elements 
to the right by `k` steps.

Sample Input:  lst = [1, 2, 3, 4, 5], k = 2
Sample Output: [4, 5, 1, 2, 3]
"""

def rotate_right(lst, k):
    # TODO: Rotate list right by k steps
    pass

# Test Q5:
# print(rotate_right([1, 2, 3, 4, 5], 2))


# ------------------------------------------------------------
# Q6. Case-Insensitive Palindrome Checker (Strings)
# ------------------------------------------------------------
"""
Problem:
Write a function `is_palindrome(s)` that ignores spaces, punctuation, 
and letter casing to check if a string is a palindrome.

Sample Input:  "A man a plan a canal Panama"
Sample Output: True
"""

def is_palindrome(s):
    # TODO: Check if s is palindrome ignoring case and spaces
    pass

# Test Q6:
# print(is_palindrome("A man a plan a canal Panama"))


# ------------------------------------------------------------
# Q7. Squares of Even Numbers (List Comprehension)
# ------------------------------------------------------------
"""
Problem:
Using List Comprehension in a single line, generate a list of squares 
for all even numbers from 1 to 20.

Sample Output: [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
"""

def get_even_squares():
    # TODO: Generate list of squares for even numbers 1..20 using list comprehension
    return []

# Test Q7:
# print(get_even_squares())


# ------------------------------------------------------------
# Q8. Safe Division Function (Exception Handling)
# ------------------------------------------------------------
"""
Problem:
Write a function `safe_divide(a, b)` that performs division `a / b`. 
Catch `ZeroDivisionError` and `TypeError` gracefully and return an error message.

Sample Call:   safe_divide(10, 0)
Sample Output: "Error: Cannot divide by zero!"
"""

def safe_divide(a, b):
    # TODO: Implement division with try-except for ZeroDivisionError and TypeError
    pass

# Test Q8:
# print(safe_divide(10, 0))


# ------------------------------------------------------------
# Q9. Count File Statistics (File Handling)
# ------------------------------------------------------------
"""
Problem:
Write a Python program that reads a text file and counts the total number of 
lines, words, and characters inside it.

Sample Output: Total Lines: 5 | Total Words: 42 | Total Characters: 215
"""

def count_file_stats(filename):
    # TODO: Read file and return lines, words, chars count
    pass

# Test Q9:
# count_file_stats("sample_data.txt")


# ------------------------------------------------------------
# Q10. Bank Account System (OOP Concepts)
# ------------------------------------------------------------
"""
Problem:
Create a `BankAccount` class with a private attribute `__balance`.
Provide methods:
  - `deposit(amount)`
  - `withdraw(amount)` (Raise custom `InsufficientBalanceError` if withdraw > balance)
  - `get_balance()`

Sample Interaction:
  account = BankAccount(1000)
  account.deposit(500)
  account.withdraw(300)
  print(account.get_balance()) # Output: 1200
"""

class InsufficientBalanceError(Exception):
    pass

class BankAccount:
    def __init__(self, initial_balance=0):
        # TODO: Define private balance attribute
        pass

    def deposit(self, amount):
        pass

    def withdraw(self, amount):
        pass

    def get_balance(self):
        pass

# Test Q10:
# account = BankAccount(1000)
# account.deposit(500)
# account.withdraw(300)
# print(account.get_balance())
