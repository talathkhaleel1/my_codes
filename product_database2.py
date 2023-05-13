# We are going to represent our products in a map where the keys are strings representing the product's name and the values are numbers representing the product's price.
#
# Create a map with the following key-value pairs.
#
# Product name (key)	Price (value)
# Eggs	200
# Milk	200
# Fish	400
# Apples	150
# Bread	50
# Chicken	550
# Create an application which solves the following problems.
#
# Which products cost less than 201? (just the name)
# Which products cost more than 150? (name + price)

products = {"Eggs":200, "Milk":200, "Fish":400, "Apples":150, "Bread": 50, "Chicken":550}

# Which products cost less than 201? (just the name)
for k,v in products.items():
    if v < 201:
        print(k)

# Which products cost more than 150? (name + price)
for k,v in products.items():
    if v > 150:
        print(k,v)
