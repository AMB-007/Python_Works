# Question: Write a Python program for pass fail lambda.

# Lambda function for conditional evaluation (Pass/Fail mark check)

check_marks = lambda mark: "Pass" if mark >= 40 else "Fail"

print("Mark 56:", check_marks(56))
print("Mark 32:", check_marks(32))

