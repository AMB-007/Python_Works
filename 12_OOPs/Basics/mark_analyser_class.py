# Question: Create a Mark_Analyser class with __init__ constructor, average calculation, and display methods.

class Mark_Analyser:
    def __init__(self, name: str, marks: list):
        self.name = name
        self.marks = marks
        self.average = 0
        print(f"Welcome {name}!")

    def calculate_average(self):
        if len(self.marks) > 0:
            self.average = sum(self.marks) / len(self.marks)
        return self.average

    def display(self):
        print(f"Student: {self.name} | Average Mark: {self.average:.2f}")

# Instance creation and method calls
user_1 = Mark_Analyser(name="Arun", marks=[50, 46, 67, 80, 98])
user_1.calculate_average()
user_1.display()
