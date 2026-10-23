from product import Product

class Inventory:
    def __init__(self, inventory_list:list[Product]):
        # To track product objects in a list
        self.__inventory_list = inventory_list

    def get_inventory_list(self):
         return self.__inventory_list

    def add_product(self, product:Product):
        self.__inventory_list.append(product)

    def search_product(self, product_id:str):
        for product in self.__inventory_list:
                if product_id == product.get_productid().lower():
                    return product
        return None

    def display_all(self):
        for product in self.__inventory_list:
             product.display_information()