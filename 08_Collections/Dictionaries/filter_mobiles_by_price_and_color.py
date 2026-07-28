# Question: Write a Python program for filter mobiles by price and color.

# Filter mobiles with price above 90k and color black

mobiles = {
    "Apple": {"model": "iPhone 13", "price": 120000, "color": "black"},
    "Samsung": {"model": "Galaxy S21", "price": 95000, "color": "white"},
    "Google": {"model": "Pixel 6", "price": 40000, "color": "black"}
}

print("Mobiles priced above 90k and black in color:")
for brand, details in mobiles.items():
    price = details.get("price")
    color = details.get("color")
    if price > 90000 and color == "black":
        print(f"- {brand}: {details}")

