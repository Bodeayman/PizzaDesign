# Welcome Again
## Bunch of the design patterns that applied to this code
### Singleton Design

#### This design pattern ensures that the class has only one instance , and everytime you try to create a new one it will refer to the same instance 
#### Talking about its application in the system , we see here that singleton applied to the inventory managment to ensure that anytime that user create a new instance it will refer to the same instance and the same inventory , and doing this will prevent creating new instances with differnet inventory forms  , which will make you confuse , which one have the correct inventory 

#### Before applying to the system , you could create any number of instances , but as normal it will create different inventories which will lead to inconsistent inventory states , making it harder to track and update

#### The singleton improves maintainability by
##### Centralized Inventory Management , as you have single instance it's going to be easier to track the changes , and you won't have duplicate instances 
###### It improve extensibility by giving global access to the inventtory , which makes any class to interact with the inventory management instance , all of them will interact with the same instance , which going to be useful if you want to add new features
###### 
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

######

### Factory Method
#### This design pattern helps in creating objects without exposing the class instantiation information to the user,

#### Talking about it's application the user have PizzaFactory class that have a create_pizza method that you pass the type of the pizza by the parameters , and if the system needs to support additional types you can easily jmodify the factory method 

#### Before applying the pattern , the code for creating different pizzas would be scattered and spreaded across the file which makes you as a developer to maintain it you will need to modifiy every line in the code
#### The factory method improved the maintainability by  centralizing pizza creation in the PizzaFactory, the system becomes more maintainable. Adding a new pizza type requires modifying only the factory class, not the rest of the system.
#### About the extensibility if you want to add new pizza types, you can do so without touching other parts of the code. The factory method encapsulates and protects the logic of the instantion of the class, so adding a new pizza type is just a matter of extending the PizzaFactory

###### 
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

#####

### Strategy method
#### The startegy design is allowing the client to choose from different strategies or behavios for the same class , it defines a family of alogirthms and makes them interchangable 
#### Like in our application, the paymentprocessor class interacts with the payment startegy interface , enabling different strategies for payment to be used dynamically
#### Before applying the algorithm , the code would likely have hard-coded conditions for handling different payment methods like if statements , making it difficult to extend to new payment methods without modifying the client code.

#### Maintainability and Extensibility 
#### The payment method logic is isolated in separate strategy classes (PayPalPayment, CreditCardPayment). To add a new payment method, you only need to create a new class that implements the PaymentStrategy interface, and no changes are needed in other parts of the system.

#### Strategy Pattern: To add a new payment method, simply create a new class that implements the PaymentStrategy interface. The rest of the code (like PaymentProcessor) does not need modification.

##### 
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
#####

#### Over-engineering happens when a solution or design becomes more complicated than it really needs to be to solve the problem. It usually means adding extra features, layers, or complexity that don't actually help with the main task. This can lead to: more Complexity: The code gets harder to understand, fix, or update. performance problems: extra layers or checks can slow things down , wasting Resources: Time, effort, and resources are spent on things that aren't necessary and less Flexibility: The solution gets so complicated that it's harder to change or improve later on.
#### singleton pattern for InventoryManager: Using a singleton (ensuring only one instance) is unnecessary. A simple class or object could work just fine without this complexity.
#### Abstract payment system (strategy pattern): the use of a separate class for each payment method is over-complicated. Just handling payments directly would be simpler.
#### checking the inventory for every topping: constantly checking if toppings are available makes the system more complex. A simpler approach could just assume toppings are available or handle shortages in a simpler way.
#### pizza factory for pizza creation: using a factory pattern to create pizzas adds extra steps. directly creating pizza objects would be easier, especially if the options are limited.
##### 
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
#####
# And that's all thank you.