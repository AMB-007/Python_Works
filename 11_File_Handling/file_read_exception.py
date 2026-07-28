# Safe file reading using try-except for FileNotFoundError handling

filename = input("Enter file name to read: ")

try:
    with open(filename, "r") as file:
        result = file.read()
        print("File Content:")
        print(result)
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")

print("File reading operation complete.")
