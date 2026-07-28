# Demonstration of file reading methods: readable(), readline(), and readlines()

file_path = "sample_read_demo.txt"

# First ensure sample content exists
with open(file_path, "w") as file:
    file.write("Line 1: Hello Python!\nLine 2: Demonstration of file read methods.\nLine 3: File handling in Python.")

# Now demonstrate read methods
with open(file_path, "r") as file:
    print("Is file readable?:", file.readable())
    file.seek(0)
    lines = file.readlines()
    print("Lines read:", lines)
