# Handling multiple exceptions (ZeroDivisionError and ValueError)

try:
    num_1 = int(input("Enter a number: "))
    print("100 / number =", 100 / num_1)
except ZeroDivisionError:
    print("Error: Zero division is not allowed.")
except ValueError:
    print("Error: Please enter a valid integer.")

print("Program execution finished.")
