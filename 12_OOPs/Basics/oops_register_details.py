# Question: Create a Details class with methods to register user details (name, age) and display them.

class Details:
    def register(self, name: str, age: int):
        self.name = name
        self.age = age
        return "Registered successfully"

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

# Object creation and execution
user = Details()
print(user.register(name="Sukumar", age=25))
user.display()
