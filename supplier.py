class Supplier:
    def __init__(self, supplier_id: str, name: str,contact_email: str):
        self.__name: str = name
        self.__supplier_id: str = supplier_id
        self.__contact_email: str = contact_email

    def display_information(self) -> None:
        print("Supplier Name: ", self.__name)
        print("Supplier ID: ", self.__supplier_id)
        print("Contact Email: ", self.__contact_email)