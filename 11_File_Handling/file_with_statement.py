# Safe file operations using 'with open()' context manager
# Context manager automatically handles file closing.

file_path = "sample_context_manager.txt"

with open(file_path, "w") as file:
    file.write("Hello, Python! Context manager handles file closing automatically.")

print(f"File {file_path} created and written safely.")
