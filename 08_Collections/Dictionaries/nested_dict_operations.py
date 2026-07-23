mobiles = {
    "Apple": {"model": "iPhone 13","price": 120000,"color": "black"},
    "Samsung": { "model": "Galaxy S21", "price": 95000, "color": "white"},
    "Google": {"model": "Pixel 6","price": 40000,"color": "black"}
}

# wap to print the model and price of each mobile in the dictionary
result = {}
for i in mobiles:
    value = mobiles.get(i)
    model = value.get("model")
    price = value.get("price")
    result[i] = [model,price]
print(result)


# wap to get the mobile model name which have price in between 50k and 1lakh

for i in mobiles:
    value = mobiles.get(i)
    model = value.get("model")
    price = value.get("price")
    if 50000 > price < 100000:
        print(model)



# wap to get the mobiles which have the price above 90k and color its black.

result = []
for i in mobiles:
    value = mobiles.get(i)
    model = value.get("model")
    color = value.get("color")
    price = value.get("price")
    if price > 100000 and color == "black":
  
        print(i,value)



