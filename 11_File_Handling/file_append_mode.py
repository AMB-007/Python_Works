# Appending data to an existing file using 'a' (Append) mode
# Note: 'a' mode appends content without overwriting existing data.

file_path = "sample_write.txt"

with open(file_path, "a") as file:
    file.write("Appended Line: Thank You!\n")

print(f"Data appended to {file_path} successfully.")
