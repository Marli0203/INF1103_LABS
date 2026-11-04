from product import Product
from canbeshipped import CanBeShipped

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, productid:str, name:str, price:float, stock:int, weight:float):
        # Initialize parent class attributes
        super().__init__(productid, name, price, stock)

        # Initialize child class attributes
        self.__weight = weight

    # This method overrides the method from the parent class
    def display_information(self):
            # Print the attributes of the Product object.
            super().display_information()
            print("|" + "Weight (KG): " + str(self.__weight))

    # Implementation of the abstract method from CanBeShipped interface
    # using our own implementation of shipping cost calculation
    def calculate_shipping_cost(self):
        multiplier = 0
        if (2 < self.__weight <= 5):
            multiplier = 0.1
        elif (5 < self.__weight <= 10):
            multiplier = 0.2
        else:
            multiplier = 0.3
        return self.__weight * multiplier

    # This method implements the abstract method from the parent class
    def get_fulfillment_info(self):
        print("This is a physical product which requires shipping.")

    def get_weight(self):
        return self.__weight
        