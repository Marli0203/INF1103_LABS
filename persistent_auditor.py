# Defining Functions
def get_valid_input():
    # Prompt User for Product Name
    product_name = input("\nEnter Product Name: ")

    # Check at this stage if user wants to quit
    if product_name.lower().strip() == "quit":
        return "quit", 0

    # Prompt User for Quantity
    quantity = input("Enter Quantity: ").lower().strip()

    # Check For Invalid Input
    if quantity != "quit" and (quantity.isdigit() == False or int(quantity) <= 0):
        print("Error: '" + quantity + "' is not a valid input!") # Print Error Message
        quantity = "invalid"
    return product_name, quantity

def process_delivery(current_total: int, new_value: int):
    # Add New Value To Current Total
    current_total += new_value
    return current_total

def calculate_tax(amount: float):
    return round(amount * 0.1, 2)

def generate_report(total_units: int, failed_attempts: int):
    print("\nTotal Units Processed:", total_units, "\nTotal Tax:", calculate_tax(float(total_units)), "\nNumber of Failed Entries:", failed_attempts)
    return

def load_inventory():
    # Create file if it does not exist
    file = open(".\\INF1103-Labs\\inventory.txt", "a")
    file.close()

    # Load transaction history
    file = open(".\\INF1103-Labs\\inventory.txt", "r")
    transaction_history = file.readlines()
    file.close()

    # Create a nested list
    transactions = []
    for entry in transaction_history:
        transactions.append(list(entry.split(",")))
        
    return transactions

def save_inventory(transaction):
    # Open the file to append existing file
    with open(".\\INF1103-Labs\\inventory.txt", "a") as file:
        # Write the transaction into inventory.txt,
        # making sure to leave a new line for
        # future additions to the inventory.txt file
        file.write(transaction + "\n")

# === Variable Initialization ===

# Track Inventory
inventory = []

# Track inventory count
inventory_count = 0

# Track the quantity that has been processed
processed_quantity = 0

# Track the number of failed attempts
failedEntriesCounter = 0

# === Main Program Flow ===
while True:
    # Load And Store Inventory Into Variable
    inventory = load_inventory()

    # Get Total Inventory Count
    inventory_count = 0
    for entry in inventory:
        # When new inventory file is initialized,
        # the data is empty. This will cause
        # problems when performing inventory count
        # as the entry will be empty. Cannot convert
        # empty into integer. So check if it is
        # not empty before converting to integer
        if len(entry) == 3:
            inventory_count += int(entry[2])

    # Display Orders
    print("Current Orders:\n")

    # Loop through each line in the text file
    for entry in inventory:
        # Print the 'ID', 'Product Name' and 'Quantity'. Remove the '\n'
        # so that the list is neater
        print((entry[0] + "," + entry[1] + "," + entry[2]).replace('\n', ''))

    # Get Product Name and Quantity
    product_name, quantity = get_valid_input()

    # If user wants to quit, break the loop
    if product_name == "quit" or quantity == "quit":
        break;

    # If quantity is invalid, add to counter
    if quantity == "invalid":
        failedEntriesCounter += 1
        continue

    # The inputs are valid. Check for inventory overflow
    if process_delivery(inventory_count, int(quantity)) > 500:
        print("Alert: Total inventory has exceeded 500 units!")
        failedEntriesCounter += 1
        break;

    # No inventory overflow. Now it is safe to call save_inventory()
    # Create transaction string
    transaction_string = str(len(inventory) + 1) + "," + product_name + "," + quantity
    save_inventory(transaction_string)

    # Update the Processed Quantity, only after saving to inventory.txt
    processed_quantity = process_delivery(processed_quantity, int(quantity))

    # Display 'New Order Added'
    print("\nNew Order Added:\n" + transaction_string)

    # Display "Order successfully saved to inventory.txt"
    print("\nOrder successfully saved to inventory.txt\n")

generate_report(processed_quantity, failedEntriesCounter)