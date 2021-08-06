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


def is_resources_enough(order_ingredient):
    """It checks the amount of resources left and return true if its enough"""
    for item in order_ingredient:
        if order_ingredient[item] >= resources[item]:
            print(f"sorry, there is not enough {item}")
            return False
    return  True


def process_coins():
    """it calculate the total amount of money inserted and return total amount"""
    print("please insert a coin")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """it add profit and also gives change to customers"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"your change is ${change}, take it.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, thats not enough money to get the drink, money refunded. ")
        return False

def make_coffe(drink_name, order_ingredients):
    for item in order_ingredients:
        resource[item] -= order_ingredients[item]
        print("your coffe is ready, take it and enjoy")


is_on = True

while is_on:
    choice = input("welcome to the coffee machine, what would you like to take? (espresso, latte, cappuccino) \n").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: {profit}")
    else:
        drink = MENU[choice]
        if is_resources_enough(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffe(choice, drink["ingredients"])




