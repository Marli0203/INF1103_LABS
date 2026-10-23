from pathlib import Path
from product import Product
from inventory import Inventory
import json

def load_inventory():
    '''
    1.  Find the inventory file.
    2.  If found, display success message.
        If not found, display missing message,
        create inventory file.
    3.  Load the inventory.
    4.  Return the inventory list.
    '''
    inventory_json = None
    
    # Step 1.
    inventory_Path = Path(".\\inventory.json")

    # Step 2.
    if inventory_Path.is_file():
        # If file exists
        print("inventory.json found.")
        file = open(".\\inventory.json", "r")
        inventory_json = json.load(file)
        file.close()
    else:
        # If file does not exist
        print("inventory.json not found.")

        # Create file if it does not exist
        file = open(".\\inventory.json", "a")
        json.dump([], file)
        file.close()
        print("inventory.json created successfully.")
        
        # Load transaction history
        file = open(".\\inventory.json", "r")
        inventory_json = json.load(file)
        file.close()

    # Step 3. Load into inventory
    products = []
    for product_json in inventory_json:
        products.append(Product(product_json["ID"],
                                product_json["Name"],
                                float(product_json["Price"]),
                                int(product_json["Stock"])))
    print("Inventory loaded successfully.\n")

    return Inventory(products)

def get_Valid_Input():
    '''
    1. Prompt for user input
    2. Loop while user input is NOT digit AND NOT within range 
    3. Re-prompt
    4. Return validated user input
    '''
    # 1. Prompt for user input
    user_Input = input("\nEnter Option: ").lower().strip()

    # 2. Loop while user input is NOT digit and NOT within range
    while user_Input.isdigit() == False or int(user_Input) > 6 or int(user_Input) < 1:
        # 3. Re-prompt for user input
        print(user_Input + " is not a valid option!")
        user_Input = input("\nEnter Option: ").lower().strip()

    # 4. Return validated user input
    return int(user_Input)

# Function for Option 1
def display_All_Products(inventory: Inventory):
    '''
    1. Display "Current Inventory" title and top line
    2. Display all products
    3. Display the bottom line
    '''
    # 1. Display title and line
    print("Current Inventory\n" +
          "----------------------------------------")

    # 2. Display all products
    inventory.display_all()

    # 3. Print bottom line
    print("----------------------------------------\n")

# Function for Option 2
def add_Product(inventory: Inventory):
    '''
    1. Display "Add New Product"
    2. Prompt for the inputs
    3. Compile into a Product object
    4. Add to inventory
    5. Display "product added successfully!
    '''
    # 1. Display "Add New Product"
    print("\nAdd New Product")

    # 2. Prompt for the inputs
    product_ID = input("Product ID: ").strip()
    product_Name = input("Product Name: ").strip()
    price = input("Price: ").lower().strip()
    stock_Quantity = input("Stock: ").lower().strip()

    # 3. Compile data into a Product object
    product_obj = Product(product_ID,
                          product_Name,
                          float(price),
                          int(stock_Quantity))

    # 4. Add to inventory
    inventory.add_product(product_obj)

    # 5. Print Success Message
    print("Product added successfully!")

    # 6. Return inventory
    return inventory

# Function for Option 3
def update_Stock(inventory: Inventory):
    '''
    1. Display "Update Stock"
    2. Prompt for product id
    3. Search through inventory for product using id
    4. If not found, show missing message then exit
    5. If found, Display product details
    6. Prompt for stock quantity (new)
    7. Update stock quantity
    8. Display "Stock updated successfully!"
    9. Return inventory
    '''
    # 1. Display "update Stock"
    print("\nUpdate Stock")

    # 2. Prompt for Product ID
    product_ID_Search = input("Enter Product ID: ").strip().lower()

    # 3. Search through inventory for a matching ID
    match_Found = inventory.search_product(product_ID_Search)

    # 4. If not found, show missing message then exit
    if match_Found == None:
        print("Product not found\n")
        return inventory

    # 5. If found, display product details
    print("\nProduct Found:" + 
          "\nName: " + match_Found.get_name() +
          "\nCurrent Stock: " + str(match_Found.get_stock()) + "\n")

    # 6. Prompt for Stock Quantity (New)
    new_Stock = input("New Stock Quantity: ").strip()

    # 7. Update Stock Quantity
    inventory.search_product(product_ID_Search).update_stock(new_Stock)

    # 8. Display successful message
    print("Stock updated successfully!")

    # 9. Return inventory
    return inventory

# Function for Option 4
def search_Product(inventory: Inventory):
    '''
    1. Display "Search Product"
    2. Prompt user for product id
    3. Search through inventory for a matching ID
    4. If not found, print missing message and exit
    5. If found, print product details
    '''
    # 1. Display "Search Product"
    print("\nSearch Product")

    # 2. Prompt for Product ID
    product_ID_Search = input("Enter Product ID: ").strip().lower()

    # 3. Search through inventory for a matching ID
    match_Found = inventory.search_product(product_ID_Search)

    # 4. If not found, print missing message and exit
    if match_Found == None:
        print("Product not found.")
        return

    # 5. If found, print product details
    print("\nProduct Found\n" +
          "----------------------------------------" +
          "\nID: " + match_Found.get_productid() +
          "\nName: " + match_Found.get_name() +
          "\nPrice: " + str(match_Found.get_price()) +
          "\nStock: " + str(match_Found.get_stock()) +
          "\n----------------------------------------\n")
    

# Function for Option 5
def save_Inventory(inventory: Inventory):
    '''
    1. Find the inventory file
    2. Save to inventory.json
    3. Display success message
    '''

    # 1. Find the Inventory File
    file = open(".\\inventory.json", "w")

    # 2. Save to inventory.json
    inventory_json = []
    for product in inventory.get_inventory_list():
        inventory_json.append({"ID": product.get_productid(),
                               "Name": product.get_name(),
                               "Price": str(product.get_price()),
                               "Stock": str(product.get_stock())})
    
    json.dump(inventory_json, file)
    file.close()

    # 3. Display success message
    print("Inventory saved successfully to inventory.json")



'''
Program Flow
1. Display App Title
2. Load inventory into a list/dictionary
3. Loop While NOT 'Exit'
4. Display Menu
5. Get User Input
6. Carry Out The Option
7. Display Thank you message.
'''

# Initialize Variables
user_Input = -1

# 1. Display App Title
print("==============================\n" +
      "INVENTORY MANAGEMENT SYSTEM\n" +
      "==============================\n")

# 2. Load Inventory
inventory = load_inventory()

# 3. Loop While NOT 'Exist'
while user_Input != 6:
    # 4. Display Menu
    print("---------- MENU ----------\n" + 
          "1. Display All Products\n" +
          "2. Add Product\n" +
          "3. Update Stock\n" +
          "4. Search Product\n" +
          "5. Save Inventory\n" +
          "6. Exit\n" +
          "--------------------------\n")

    # 5. Get User Input
    user_Input = get_Valid_Input()

    # 6. Carry out functions based on option
    match user_Input:
        case 1:
            display_All_Products(inventory)
        case 2:
            inventory = add_Product(inventory)
        case 3:
            inventory = update_Stock(inventory)
        case 4:
            search_Product(inventory)
        case 5:
            print("\nSaving inventory...")
            save_Inventory(inventory)
        case 6: 
            print("\nSaving inventory before exit")
            save_Inventory(inventory)
# 7. Display Thank You Message
print("Thank you for using Inventory Management System.\nProgram terminated.")