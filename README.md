# Coffee_Machine_Simulation
This is a simple coffee machine simulation written in Python. The program allows users to select different types of coffee (espresso, latte, cappuccino) and handles the resources, payments, and change.

Features
User can choose from different types of coffee drinks (espresso, latte, cappuccino).
The program checks whether there are enough resources (water, milk, coffee) to make the selected coffee.
Users can insert coins (quarters, dimes, nickels, pennies) to pay for the coffee.
The program calculates and returns change if the payment exceeds the coffee cost.
The coffee machine maintains resources and updates them after each coffee purchase.
Users can view a report showing the current available resources (coffee, water, milk) in the machine.
How to Use
Run the coffee_machine.py script in your Python environment.
Follow the instructions on the console to select a coffee, insert coins, and receive your coffee and change.
Enter "report" to view the current available resources in the coffee machine.
Enter "off" to turn off the coffee machine.
Dependencies
The script uses the menu module, which contains a dictionary of coffee menu items and their ingredients.
The resources dictionary holds the initial quantities of water, milk, and coffee available in the coffee machine.
