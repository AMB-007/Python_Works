# Question: Create a Calculator class with methods to return the sum and product of two numbers.

class Calculator:
    def add_num(self, num_1, num_2):
        return num_1 + num_2

    def product(self, num_1, num_2):
        return num_1 * num_2

# Object creation and method invocation
obj1 = Calculator()
print("Addition result:", obj1.add_num(3, 4))
print("Product result:", obj1.product(4, 5))
