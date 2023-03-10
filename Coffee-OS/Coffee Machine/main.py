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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

cont = True
cost = 0

while cont:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()


    def user_input_check(coffee_type):
        """Collects the user input, verify the type of coffee and returns the coffee ingredient from the dictionary"""
        if coffee_type == "report" or coffee_type == "off":
            return resources
        else:
            return MENU[coffee_type]


    if user_input != "report" and user_input != "off":
        ingredients = user_input_check(user_input)["ingredients"]

        water = resources["water"]
        milk = resources["milk"]
        coffee = resources["coffee"]


        def ingredients_check():
            """It will return True if resources are enough and returns False if resources are not enough"""
            for keys in ingredients:
                if keys == "water" and water >= ingredients["water"]:
                    continue
                elif keys == "milk" and milk >= ingredients["milk"]:
                    continue
                elif keys == "coffee" and coffee >= ingredients["coffee"]:
                    continue
                else:
                    return False
            return True


        def cost_check(coffee_type):
            """Collects the user input as its input and returns the cost of the user input"""
            return MENU[coffee_type]["cost"]


        static_cost = cost_check(user_input)    # Retrieve cost from dictionary
        cost += static_cost    # Changes with every iteration
        in_check = ingredients_check()  # Calling the function for if resources are enough

        # If resources are enough, it'll subtract from the resources and replace the value
        if in_check:
            for key in ingredients:
                if key == "water":
                    water = water - ingredients["water"]
                    resources["water"] = water
                elif key == "milk":
                    milk = milk - ingredients["milk"]
                    resources["milk"] = milk
                elif key == "coffee":
                    coffee = coffee - ingredients["coffee"]
                    resources["coffee"] = coffee

            # How much you want to pay
            print("Please insert coins.")
            quarters = float(input("how many quarters?: ")) * 0.25
            dimes = float(input("how many dimes?: ")) * 0.1
            nickles = float(input("how many nickles?: ")) * 0.05
            pennies = float(input("how many pennies?: ")) * 0.01
            total_cost = quarters + dimes + nickles + pennies

            # If money is enough or not
            if total_cost >= static_cost:
                change = round(total_cost - static_cost, 2)
                print(f"Here is ${change} in change.")
                print(f"Here is your {user_input} ☕️. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")

        # If resources are not enough
        else:
            if water < ingredients["water"]:
                print("Sorry there is not enough water.")
            elif milk < ingredients["milk"]:
                print("Sorry there is not enough milk.")
            else:
                print("Sorry there is not enough coffee.")

    # If user inputs "report"
    elif user_input == "report":
        if cost == 0:
            pass
        else:
            resources["Money"] = "$" + str(cost)
        for key, value in resources.items():
            if key == "water" or key == "milk":
                print(f"{key}: {value}ml")
            elif key == "coffee":
                print(f"{key}: {value}g")
            else:
                print(f"{key}: {value}")

    # If user inputs "off"
    if user_input == "off":
        break
    else:
        user_input_check(user_input)
