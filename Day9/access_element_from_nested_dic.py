order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}

## Which Line of code will print : "Steak"
print(order["main"][2])    # This will print ['Steak']
print(order["main"][2][0])  ## This will print element value