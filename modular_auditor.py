#This is the code for INF 1103 Lab 2

# Defining Functions
def get_valid_input():
    return

def process_delivery(current_total: int, new_value: int):
    return

def calculate_tax(amount: float):
    return

def generate_report(total_units: int, failed_attempts: int):
    return

#Requirement 1
inventory = 0
failedEntriesCounter = 0

#Requirement 2
while True:
    #Get User Input and "Clean" It
    stock = input("Enter a stock quantity: ").lower().strip()

    if stock == "quit":
        break;

    #Requirement 4 and Requirement 5
    if stock.isdigit() == False or int(stock) < 0:
        print("Error: '" + stock + "' is not a valid input!")
        failedEntriesCounter += 1
        continue

    #Requirement 3
    stock = int(stock)

    #Requirement 6
    inventory += stock

    #Requirement 7
    if inventory > 500:
        print("Alert: Total inventory has exceeded 500 units!")
        failedEntriesCounter += 1
        break;

#Requirement 8
print("\nTotal Units Processed:", inventory, "\nNumber of Failed Entries:", failedEntriesCounter)