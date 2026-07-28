# Question: Write a Python program for nested dict operations.

# Extract model name and price from a nested dictionary of mobiles

mobiles = {
    "Apple": {"model": "iPhone 13", "price": 120000, "color": "black"},
    "Samsung": {"model": "Galaxy S21", "price": 95000, "color": "white"},
    "Google": {"model": "Pixel 6", "price": 40000, "color": "black"}
}

result = {}
for brand, details in mobiles.items():
    model = details.get("model")
    price = details.get("price")
    result[brand] = [model, price]

print("Mobile Model and Price:", result)

