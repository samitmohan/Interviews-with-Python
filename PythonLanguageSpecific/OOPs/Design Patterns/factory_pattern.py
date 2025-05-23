from abc import ABC, abstractmethod
"""
The Factory Pattern is a creational design pattern that provides an interface for creating objects
without specifying their exact classes. It encapsulates object creation logic and promotes loose 
coupling between the client code and the concrete classes.
"""
class Pizza:
    def __init__(self, ingredients) -> None:
        self.ingredients = ingredients

    def __repr__(self) -> str:
        return f"{self.ingredients}"
    
    # factory methods
    # Each method encapsulates the creation logic for specific pizza types
    @classmethod
    def margherita(cls):
        return cls(["ingredients for margherita"])
    
    @classmethod
    def napolean(cls):
        return cls(["ingredients for napolean"])
    
    @classmethod
    def thincrust(cls):
        return cls(["ingredients for thincrust"])
    
print(Pizza.margherita())
print(Pizza.napolean())

"""
When you need to create objects but don't know the exact types until runtime
When object creation involves complex logic
When you want to centralize object creation
When you need to support multiple product families (Abstract Factory)
When you want to make your code more testable by injecting mock factories
"""

# A better example in place.

class PizzaCreator:
    @abstractmethod
    def create_pizza(self) -> Pizza:
        pass

    def order_pizza(self) -> None:
        print(f"Preparing {self.create_pizza()}")
        print("Ready")
        return Pizza

class MargerhitaCreator(PizzaCreator):
    def create_pizza(self) -> Pizza:
        return Pizza(["ingredients for Margerhita"])
    
class PepperoniCreator(PizzaCreator):
    def create_pizza(self) -> Pizza:
        return Pizza(["ingredients for Pepperoni"])
    
class ThinCrustCreator(PizzaCreator):
    def create_pizza(self) -> Pizza:
        return Pizza(["ingredients for Thin Crust"])
    

margherita_creator = MargerhitaCreator()
pepperoni_creator = PepperoniCreator()

pizza1 = margherita_creator.order_pizza()
pizza2 = pepperoni_creator.order_pizza()


    








    

