from product import Product

class DigitalProduct(Product):
    def __init__(self, productid:str, name:str, price:float, stock:int, download_size: float):
        # Initialize the parent class attributes
        super().__init__(productid, name, price, stock)

        # Initialize the child class attributes
        self.__download_size = download_size

    # This method overrides the method from the parent class
    def display_information(self):
                # Print the attributes of the Product object.
                print("ID: " + self.get_productid() + "|" +
                              "Name: " + self.get_name() + "|" +
                              "Price: $" + str(self.get_price()) + "|" + 
                              "Stock: " + str(self.get_stock()) + "|" +
                              "Download Size: " + str(self.__download_size))