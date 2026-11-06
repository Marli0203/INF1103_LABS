class Supplier:
    def __init__(self, supplier_id: str, name: str,contact_email: str):
        self.__name = name
        self.__supplier_id = supplier_id
        self.__contact_email = contact_email

    def display_information(self):
        print("Supplier Name: ", self.__name)
        print("Supplier ID: ", self.__supplier_id)
        print("Contact Email: ", self.__contact_email)