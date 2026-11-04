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
            print("ID: " + self.get_productid() + "|" +
                          "Name: " + self.get_name() + "|" +
                          "Price: $" + str(self.get_price()) + "|" + 
                          "Stock: " + str(self.get_stock()) + "|" +
                          "Weight: " + str(self.__weight))