MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources(order_ingredients):
    for items in order_ingredients:
        if order_ingredients[items] > resources[items]:
            print("Sorry there is not enough water.")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters? ")) * 0.25
    dimes = int(input("How many dimes? ")) * 0.10
    nickels = int(input("How many nickels? ")) * 0.05
    pennies = int(input("How many pennies? ")) * 0.01
    return quarters + dimes + nickels + pennies


def make_coffee(drink_name, order_ingredients):
    for items in order_ingredients:
        resources[items] -= order_ingredients[items]
    print(f"“Here is your {drink_name}☕. Enjoy")


while True:
    order = input("What would you like? (espresso/latte/cappuccino):")
    if order == "off":
        break

    elif order == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee:{resources['coffee']}g")
        print(f"Money: ${profit}")

    elif order in MENU:
        drink = MENU[order]
        if check_resources(drink["ingredients"]):
            coins = process_coins()
            if coins > MENU[order]["cost"]:
                coins -= MENU[order]["cost"]
                profit += MENU[order]["cost"]
                x = round(coins, 2)
                print(f"Here is ${x} in change.")
                make_coffee(order, drink["ingredients"])

            else:
                print("Sorry that's not enough money. Money refunded")
        else:
            print("Order canceled due to insufficient resources.")
    else:
        print("Invalid selection. Please choose from espresso, latte, cappuccino, or type 'off' to exit.")