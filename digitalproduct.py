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
        super().display_information()
        print("|" + "Download Size: " + str(self.__download_size))