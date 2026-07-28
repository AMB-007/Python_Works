# Question: Write a Python program for filter mobiles by price range.

# Filter mobile model names with price between 50k and 100k

mobiles = {
    "Apple": {"model": "iPhone 13", "price": 120000, "color": "black"},
    "Samsung": {"model": "Galaxy S21", "price": 95000, "color": "white"},
    "Google": {"model": "Pixel 6", "price": 40000, "color": "black"}
}

print("Mobiles priced between 50k and 100k:")
for brand, details in mobiles.items():
    model = details.get("model")
    price = details.get("price")
    if 50000 <= price <= 100000:
        print(f"- {model} (Rs. {price})")

