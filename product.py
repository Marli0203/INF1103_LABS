class Product:
    def __init__(self, productid:str, name:str, price:float, stock:int):
        # Initialize the attributes of a general Product object
        self.__productid = productid
        self.__name = name
        self.__price = price
        self.__stock = stock

    def get_productid(self):
        # Encapsulation: Developers use this public method instead of directly
        #                accessing the attribute.
        return self.__productid

    def get_name(self):
        # Encapsulation: Developers use this public method instead of directly
        #                accessing the attribute.
        return self.__name

    def get_price(self):
        # Encapsulation: Developers use this public method instead of directly
        #                accessing the attribute.
        return self.__price

    def get_stock(self):
        # Encapsulation: Developers use this public method instead of directly
        #                accessing the attribute.
        return self.__stock

    def update_stock(self, quantity:int):
        # Encapsulation: Developers use this public method instead of directly
        #                accessing the attribute to update the stock.
        self.__stock = quantity

    def display_information(self):
        # Print the attributes of the Product object.
        print("ID: " + self.__productid + "|" +
                      "Name: " + self.__name + "|" +
                      "Price: $" + str(self.__price) + "|" + 
                      "Stock: " + str(self.__stock))