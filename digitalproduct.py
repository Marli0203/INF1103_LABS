from product import Product
from supplier import Supplier

class DigitalProduct(Product):
    def __init__(self, productid:str, name:str, price:float, stock:int, supplier: Supplier, download_size: float):
        # Initialize the parent class attributes
        super().__init__(productid, name, price, stock, supplier)

        # Initialize the child class attributes
        self.__download_size = download_size

    # This method overrides the method from the parent class
    def display_information(self):
        # Print the attributes of the Product object.
        super().display_information()
        print("|" + "Download Size: " + str(self.__download_size))

    # This method implements the abstract method from the parent class
    def get_fulfillment_info(self):
            print("This is a digital product which is delivered digitally.")

    def get_download_size(self):
         return self.__download_size