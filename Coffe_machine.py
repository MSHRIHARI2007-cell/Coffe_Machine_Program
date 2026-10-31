from cfonts import render
from Coffe_Menu import MENU
from Coffe_Menu import resources

output = render("Coffe Machine Game !", font="shade")
print(output)

def is_resources_suffecient(order_ingrediants):
    """Return True when order can be made,False if ingrediants are insuffecient"""
    for item in order_ingrediants:
        if order_ingrediants[item] > resources[item]:
            print(f"Sorry ther is not enough {item}.")
            return False
    return True

def process_coins():
        """Return the total calculated from Coins inserted."""
        print("Please insert coins.")
        quaters = int(input("How many Quaters?: ")) * 0.25
        dimes = int(input("How many Dimes?: ")) * 0.1
        nickels = int(input("How many Nickels?: ")) * 0.05
        pennies = int(input("How many Pennies?: ")) * 0.01
        
        total = (quaters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
        
        return total

def is_transaction_successfull(money_recieved,drink_cost):
     """Return true when payment is accepeted or false 
            if the money is insuffecient"""
     if money_recieved >= drink_cost:
         change = round(money_recieved - drink_cost, 2)
         print(f"Here is ${change} in change.")
         global profit
         profit += drink_cost
         return True
     else:
          print("Sorry insuffecient money! Money refunded")
          return False

def make_coffee(order_ingredients):
    """Deduct the ingredients used."""

    for item in order_ingredients:
        resources[item] -= order_ingredients[item]

    print("Here is your coffee ☕ Enjoy!")

is_on = True

profit = 0

while is_on:
    choice = input("What would you Like ?(espresso/double espresso/latte/cappuccino/americano/mocha/flat white/macchiato/cartado/vanilla latte/caramel latte/hazelnut latte/chocolate coffee/iced coffee/iced mocha):")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water : {resources['water']}")
        print(f"Milk : {resources['milk']}")
        print(f"Coffe : {resources['coffe']}")
        print(f"Money : {profit}")

    elif choice in MENU:
        drink = MENU[choice]
        if is_resources_suffecient(drink["ingredients"]):
             payment = process_coins()
             if is_transaction_successfull(payment,drink["cost"]):
                  make_coffee(drink["ingredients"])
    else:
         print("Invalid choice. Please select a drink from the menu")
     