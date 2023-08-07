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


def check_resource():
    global on
    # TODO check resources are enough for the user input
    if user_input== "espresso" or user_input=="latte" or user_input=="cappuccino":
     if MENU[user_input]["ingredients"]["water"] > resources["water"]:
        print("Sorry there is no enough water !! ")
        on = False

     if user_input != "espresso":
        MENU[user_input]["ingredients"]["milk"] > resources["milk"]
        print("Sorry there is no enough milk !! ")
        on = False

     if MENU[user_input]["ingredients"]["coffee"] > resources["coffee"]:
        print("Sorry there is no enough coffee !! ")
        on = False

def check_cash():
    global on
    cash = user_quarter*0.25+ user_dimes*0.10+user_pennies*0.05+user_pennies*0.01
    if MENU[user_input]["cost"] > cash:
     print( "\nSorry that's not enough money, Money refunded.")
     on = False
    elif MENU[user_input]["cost"] < cash:
        change = round(cash- MENU[user_input]["cost"],2)
        return change

def update_resource():
    if user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
     resources["water"]= resources["water"]-MENU[user_input]["ingredients"]["water"]
     resources["coffee"]=resources["coffee"]-MENU[user_input]["ingredients"]["coffee"]
     if user_input != "espresso":
        resources["milk"]=resources["milk"]-MENU[user_input]["ingredients"]["milk"]
def report_resource():
    update_resource()
    print(f'\n Water: {resources["water"]} ml ')
    if user_input != "espresso":
       print(f'\n Milk: {resources["milk"]} ml. ')
    print(f'\n Coffee: { resources["coffee"] } g. ')

on = True
while on:
 user_input = input(" What would you like? (espresso/latte/cappuccino): ").lower()
 if user_input == "report" :
     report_resource()
     break
 if user_input == "off" :
     break
 check_resource()
 if not on:
  break

 update_resource()

 user_quarter = int(input("Insert coins please.\nHow many quarters are you going to put: "))
 user_dimes =int(input("How many dimes are you going to insert: "))
 user_nickels=int(input("How many nickels are you going to insert: "))
 user_pennies= int(input("How many pennies are you going to insert: "))

 check_cash()
 if  not on:
     break
 print(f"\n Here is ${check_cash()} dollars in change.\nHere is your {user_input}. Enjoy!")




