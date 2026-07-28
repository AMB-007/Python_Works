# Handling KeyError with finally block when accessing dictionary keys

elements = {"name": "arun", "age": 23, "place": "cochin"}
key = input("Enter key to lookup: ")

try:
    print("Value:", elements[key])
except KeyError:
    print("Error: Key not found in dictionary.")
finally:
    print("Finally block: Key lookup operation finished.")
