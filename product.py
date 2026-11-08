from abc import ABC, abstractmethod
from supplier import Supplier

class Product(ABC):
    def __init__(self, productid:str, name:str, price:float, stock:int, supplier: Supplier):
        # Initialize the attributes of a general Product object
        self.__productid: str = productid
        self.__name: str = name
        self.__price: float = price
        self.__stock: int = stock
        self.__supplier: Supplier = supplier

    def get_productid(self) -> str:
        # Encapsulation: Developers use this public method instead of directly
        #                accessing the attribute.
        return self.__productid

    def get_name(self) -> str:
        # Encapsulation: Developers use this public method instead of directly
        #                accessing the attribute.
        return self.__name

    def get_price(self) -> float:
        # Encapsulation: Developers use this public method instead of directly
        #                accessing the attribute.
        return self.__price

    def get_stock(self) -> int:
        # Encapsulation: Developers use this public method instead of directly
        #                accessing the attribute.
        return self.__stock

    def update_stock(self, quantity:int) -> None:
        # Encapsulation: Developers use this public method instead of directly
        #                accessing the attribute to update the stock.
        self.__stock = quantity

    def get_supplier(self) -> Supplier:
        # Encapsulation: Developers use this public method instead of directly
        #                accessing the attribute to update the stock.
        return self.__supplier

    def display_information(self) -> None:
        # Print the attributes of the Product object.
        print("ID: " + self.__productid + "|" +
                      "Name: " + self.__name + "|" +
                      "Price: $" + str(self.__price) + "|" + 
                      "Stock: " + str(self.__stock), end="")

    # Create the abstract method to force child classes to implement this
    @abstractmethod
    def get_fulfillment_info(self):
        pass