weight_kg = float(input("Enter the weight kg:"))
height = float(input("Enter the height cm:"))

height_m = height / 100
bmi = weight_kg / (height_m ** 2)
print(bmi)