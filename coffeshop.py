import os

class coffee:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_info(self):
        print(f"Coffee Name: {self.name}, Price: ${self.price:.2f}")


class coffee_shop:
    def __init__(self):
        self.menu = []
        self.order = []

    def add_coffee(self, coffee):
        self.menu.append(coffee)

    def display_menu(self):
        print("Coffee Shop Menu:")
        for coffee in self.menu:
            coffee.display_info()

    def order_coffee(self, coffee_name):
        for coffee in self.menu:
            if coffee.name.lower() == coffee_name.lower():
                self.order.append(coffee)   
                print(f"Order placed for: {coffee.name}, Price: ${coffee.price:.2f}")
                return
        print(f"Sorry, {coffee_name} is not available in the menu.")

    def display_order(self):
        if not self.order:
            print("No orders placed yet.")
            return
        print("Current Orders:")
        for coffee in self.order:
            coffee.display_info()
        print("\n")

    def calculate_total(self, orders):
        total = 0
        for order in orders:
            for coffee in self.menu:
                if coffee.name.lower() == order.lower():
                    total += coffee.price
                    break
        print(f"Total amount for the order: ${total:.2f}")

    def checkout(self, orders):
        total = 0
        for order in orders:
            for coffee in self.menu:
                if coffee.name.lower() == order.lower():
                    total += coffee.price
                    break
        print(f"Total amount for the order: ${total:.2f}")
        print("Thank you for your purchase!")

if __name__ == "__main__":
    shop = coffee_shop()
    shop.add_coffee(coffee("Espresso", 2.50))
    shop.add_coffee(coffee("Latte", 3.50))
    shop.add_coffee(coffee("Cappuccino", 3.00))


    while True:
        shop.display_menu()
        user_input = input("\nEnter the name of the coffee you want to order (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            if shop.order:
                shop.checkout([coffee.name for coffee in shop.order])
                break
            print("Thank you for visiting the coffee shop!")
            break

        shop.order_coffee(user_input)
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console for better readability
        shop.display_order()
        
        