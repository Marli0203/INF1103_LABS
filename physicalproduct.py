from product import Product

class PhysicalProduct(Product):
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