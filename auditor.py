#This is the code for INF 1103 Lab 2

#Requirement 1
inventory = 0

#Requirement 2
while True:
    #Get User Input and "Clean" It
    stock = input("Enter a stock quantity: ").lower().strip()

    if stock == "quit":
        break;

    #Requirement 4
    if stock.isdigit() == False:
        print("Error: '" + stock + "' is not a valid numerical input!")
        continue

    #Requirement 3
    stock = int(stock)
