# Demonstration of importing functions from a custom Python package (calculator)

from calculator import addition, subtraction

res1 = addition.add_num(2, 4)
print("Addition result:", res1)

res2 = subtraction.substract(10, 4)
print("Subtraction result:", res2)
