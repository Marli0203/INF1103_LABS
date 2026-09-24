# Defining Functions
def get_valid_input():
    # Prompt User for Input
    user_input = input("Enter a stock quantity: ").lower().strip()

    # Check For Invalid Input
    if user_input != "quit" and (user_input.isdigit() == False or int(user_input) <= 0):
        print("Error: '" + user_input + "' is not a valid input!") # Print Error Message
        user_input = "invalid"
    return user_input

def process_delivery(current_total: int, new_value: int):
    # Add New Value To Current Total
    current_total += new_value
    return current_total

def calculate_tax(amount: float):
    return amount * 0.1

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

# === Variable Initialization ===

# Load And Store Inventory Into Variable
inventory = load_inventory()

# Get Total Inventory Count
inventory_count = 0
for entry in inventory:
    inventory_count += int(entry[2])

failedEntriesCounter = 0

# Main Program Flow
while True:
    # Display Orders
    print("Current Orders:\n")
    for entry in inventory:
        print(entry[0] + "," + entry[1] + "," + entry[2])

    
    
    user_input = get_valid_input()

    if user_input == "quit":
        break;
    
    if user_input == "invalid":
        failedEntriesCounter += 1
        continue

    if process_delivery(inventory_count, int(user_input)) > 500:
        print("Alert: Total inventory has exceeded 500 units!")
        failedEntriesCounter += 1
        break;
    
    inventory = process_delivery(inventory_count, int(user_input))

generate_report(inventory_count, failedEntriesCounter)