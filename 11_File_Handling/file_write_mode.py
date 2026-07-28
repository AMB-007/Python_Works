# Writing data to a file using 'w' (Write) mode
# Note: 'w' mode overwrites existing content or creates a new file if absent.

file_path = "sample_write.txt"

with open(file_path, "w") as file:
    file.write("Hello World! Writing initial content to file.\n")

print(f"Data written to {file_path} successfully.")
