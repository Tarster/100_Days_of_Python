


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

is_on = True
profit = 0

def check_resources(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def make_coffee(drink_name, order_ingredients,money_received,drink_cost):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    global profit
    profit += MENU[coffee]["cost"]
    change = round(money_received - drink_cost, 2)
    print(f"Here is ${change} in change.")
    print(f"Here is your {drink_name} ☕️. Enjoy!")

while is_on:
    flag = False
    coffee = input("What would you like? (espresso/latte/cappuccino): ")
    if coffee == "off":
        is_on = False
    elif coffee =="report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}") 
    else:
        print("Please insert coins.")
        quarters = int(input("how many quarters?: "))
        dimes = int(input("how many dimes?: "))
        nickles = int(input("how many nickles?: "))
        pennies = int(input("how many pennies?: "))

        money = (0.01 * pennies) + (0.05 * nickles) + (0.10 * dimes) + (0.25 * quarters) 

        if money < MENU[coffee]["cost"]:
            print("Sorry that's not enough money. Money refunded.")
        else:
            
            enough_ingredient = check_resources(MENU[coffee]["ingredients"])
            
            if enough_ingredient:
                make_coffee(coffee, MENU[coffee]["ingredients"],money,MENU[coffee]["cost"])
            else:
                print("Not enough resources. Money refunded.")
                