#This is the code for INF 1103 Lab 2

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

# Lab2: Requirement 1
inventory = 0
failedEntriesCounter = 0

while True:
    # Lab3: Requirement 1
    user_input = get_valid_input()

    # Lab2: Requirement 2
    if user_input == "quit":
        break;
    
    if user_input == "invalid":
        failedEntriesCounter += 1
        continue

    # Lab3: Requirement 2
    if process_delivery(inventory, int(user_input)) > 500:
        print("Alert: Total inventory has exceeded 500 units!")
        failedEntriesCounter += 1
        break;
    
    inventory = process_delivery(inventory, int(user_input))

# Lab3: Requirement 4 (Requirement 3 in line 23)
generate_report(inventory, failedEntriesCounter)