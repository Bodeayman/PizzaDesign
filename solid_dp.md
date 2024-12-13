#### For each design pattern applied in your pizza restaurant ordering system, describe which SOLID principles the pattern addresses or aligns with. Explain how the pattern helps implement these principles in your code, in the SOLID_DP.md file.


# in our SingleTon design system 
## The Single Responsibility and the Dependency Inversion is applied 
### the inventory management class is responsible for managing inventory, and using a Singleton ensures that the class maintains a single responsibility of managing inventory across the entire system, without duplicating or complicating inventory states. (Single instance)

###  The InventoryManager is a central component, and using a Singleton provides a global point of access to the inventory system, allowing other components (like the pizza class) to interact with it without depending on multiple instances.


# In Factory design pattern
## Open/Closed principle and liskov substitution principle
### Open/Closed principle , the pizzafactory is designed to create pizza based on specific types , the class is open for extension (like you can add more types of pizza)but closed for modifiction (You can't edit the function and the logic)
### Liskov substitution principle by using PizzaFactoy , we ensure that all subclasses like the different types of pizza can be substituted in the system without affecting the behaviour of the whole system

# In Strategy design pattern
## Interface Segregation and Dependency Inversion 
### The payment strategy interface ensures the payment methods are broken into different behaviours , each referes to a speicific payment , Which keeps the classes focused and managable
### The paymentProcessor depends on the abstraction of Payment Strategy rather than using fully implemented payment class this will allow for easy substitution of different payment methods