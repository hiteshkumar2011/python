from data import MENU,resources
is_on =True
profit = 0 

def check_resources(order_ingredients):
    """ Check Resources will return True if enough resources otherwise
        will return False if insufficient resources """
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True 

def process_coins():
    """ It will return the total of money received """
    print(f"Please Insert the coins")
    total = int(input("how many quarters ?")) *0.25
    total += int(input("how many dimes ?")) * 0.1
    total += int(input("how many nickles ?")) * 0.05
    total += int(input("how many pennies ?")) * 0.01
    return total 

def is_transaction_successful(money_received,drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost,2)
        print(f"Please collect your change ${change}")
        global profit
        profit += drink_cost
        return True
    else:
        print(f"Sorry that's not enough money,Money is Refunded")
        return False

def make_coffee(drink_name,order_ingredients):
    """ Deduct ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")



while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False 
    elif choice == "report":
       print(f"Water: {resources['water']} ml")
       print(f"Milk: {resources['milk']}ml")
       print(f"Coffee: {resources['coffee']}ml")
       print(f"Money: {profit}")
    else:
        drink = MENU[choice]
        #print (drink)
        if check_resources(drink["ingredients"]):
            payment = process_coins()
            is_transaction_successful(payment,drink["cost"])
            make_coffee(choice,drink["ingredients"])

        

