# Handling IndexError with finally block when accessing list elements by index

words = ["python", "java", "c++", "javascript", "ruby"]

try:
    index = int(input("Enter index position: "))
    print("Element at index:", words[index])
except IndexError:
    print("Error: Index position out of range.")
except ValueError:
    print("Error: Invalid integer index.")
finally:
    print("Finally block: Execution completed.")
