#This is the code for INF 1103 Lab 2

# Defining Functions
def get_valid_input(failedEntriesCounter):
    # Prompt User for Input
    user_input = input("Enter a stock quantity: ").lower().strip()

    # Check For Invalid Input
    if user_input != "quit" and (user_input.isdigit() == False or int(user_input) <= 0):
        print("Error: '" + user_input + "' is not a valid input!") # Print Error Message
        failedEntriesCounter += 1
        user_input, failedEntriesCounter = get_valid_input(failedEntriesCounter); #Re-prompt
    return user_input, failedEntriesCounter

def process_delivery(current_total: int, new_value: int):
    # Add New Value To Current Total
    current_total += new_value
    return current_total

def calculate_tax(amount: float):
    return

def generate_report(total_units: int, failed_attempts: int):
    return

# Lab2: Requirement 1
inventory = 0
failedEntriesCounter = 0

# Lab2: Requirement 2
while True:
    # Lab3: Requirement 1
    user_input, failedEntriesCounter = get_valid_input(failedEntriesCounter)
    if user_input == "quit":
        break;

    # Lab3: Requirement 2
    if process_delivery(inventory, int(user_input)) > 500:
        print("Alert: Total inventory has exceeded 500 units!")
        failedEntriesCounter += 1
        break;

    inventory = process_delivery(inventory, int(user_input))

# Lab2: Requirement 8
print("\nTotal Units Processed:", inventory, "\nNumber of Failed Entries:", failedEntriesCounter)