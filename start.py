from abc import ABC, abstractmethod


# Singleton Inventory Manager
class InventoryManager:
    _instance = None  

    def __init__(self):
        if InventoryManager._instance is not None:
            raise Exception("This is a Singleton class. Use get_instance() to access the instance.")
        else:
            self.inventory = {
                "Margherita": 10,
                "Pepperoni": 10,
                "Cheese": 15,
                "Olives": 10,
                "Mushrooms": 12,
            }
            print("Inventory Manager created.")

    @staticmethod
    def get_instance():
        if InventoryManager._instance is None:
            InventoryManager._instance = InventoryManager()
        return InventoryManager._instance

    def check_and_decrement(self, item) -> bool:
        if self.inventory.get(item, 0) > 0:
            self.inventory[item] -= 1
            return True
        return False

    def get_inventory(self):
        return self.inventory

    def add_ingredient(self, ingredient, quantity):
        if ingredient in self.inventory:
            self.inventory[ingredient] += quantity
        else:
            self.inventory[ingredient] = quantity
        print(f"Added {quantity} of {ingredient}. Total: {self.inventory[ingredient]}")


# Pizza Class
class Pizza:
    def __init__(self, base_type, base_price):
        self.base_type = base_type
        self.base_price = base_price
        self.toppings = []
    
    def add_topping(self, topping_name, topping_price, inventory_manager):
        if inventory_manager.check_and_decrement(topping_name):
            self.toppings.append((topping_name, topping_price))
            print(f"Added {topping_name} to your pizza.")
        else:
            print(f"Failed to add {topping_name} due to stock shortage.")
    
    def calculate_total_cost(self):
        total_cost = self.base_price
        total_cost += sum(topping[1] for topping in self.toppings)
        return total_cost
    
    def show(self):
        description = f"Pizza base: {self.base_type}"
        for topping, _ in self.toppings:
            description += f" + {topping}"
        total_cost = self.calculate_total_cost()
        return f"{description}\nTotal cost: ${total_cost:.2f}"

class PizzaFactory:
    def create_pizza(self, pizza_type):
        if pizza_type == "Margherita":
            return Pizza("Margherita", 5)
        elif pizza_type == "Pepperoni":
            return Pizza("Pepperoni", 6)
        else:
            return None


class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying ${amount} via PayPal")
        print("Payment is successful.")


class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying ${amount} via Credit Card")
        print("Payment is successful.")


class PaymentProcessor:
    def __init__(self, payment_strategy: PaymentStrategy):
        self.payment_strategy = payment_strategy
    
    def execute_payment(self, amount):
        self.payment_strategy.pay(amount)


# Main Function
def main():
    inventory_manager = InventoryManager.get_instance()
    inventory_manager2 = InventoryManager.get_instance()
    
    pizza_factory = PizzaFactory()
    
    print("Welcome to the Pizza Restaurant!")

    while True:
        print("\nChoose your base pizza:")
        print("1. Margherita ($5.0)")
        print("2. Pepperoni ($6.0)")
        print("0 => to exit")
        pizza_choice = input("Enter the number of your choice: ")
        if pizza_choice == '0':
            break
        
        if pizza_choice == '1':
            pizza = pizza_factory.create_pizza("Margherita")
        elif pizza_choice == '2':
            pizza = pizza_factory.create_pizza("Pepperoni")
        else:
            print("Invalid pizza choice!")
            continue
        
        while True:
            print("\nAvailable toppings:")
            print("1. Cheese ($1.0)")
            print("2. Olives ($0.5)")
            print("3. Mushrooms ($0.7)")
            print("4. Finish order")
            topping_choice = input("Enter the number of your choice: ")

            if topping_choice == "1":
                pizza.add_topping("Cheese", 1.0, inventory_manager)
            elif topping_choice == "2":
                pizza.add_topping("Olives", 0.5, inventory_manager)
            elif topping_choice == "3":
                pizza.add_topping("Mushrooms", 0.7, inventory_manager)
            elif topping_choice == "4":
                break
            else:
                print("Invalid topping choice!")

        print("\nYour order:")
        print(pizza.show())

        print("\nChoose a payment method:")
        print("1. PayPal")
        print("2. Credit Card")
        payment_choice = input("Enter the number of your choice: ")

        if payment_choice == '1':
            payment_processor = PaymentProcessor(PayPalPayment())
        elif payment_choice == '2':
            payment_processor = PaymentProcessor(CreditCardPayment())
        else:
            print("Invalid payment choice!")
            continue

        payment_processor.execute_payment(pizza.calculate_total_cost())

      


if __name__ == "__main__":
    main()
