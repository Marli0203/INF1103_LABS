#This is the code for INF 1103 Lab 2

#Requirement 1
inventory = 0

#Requirement 2
stock = ""

while stock != "quit":
    #Get User Input and "Clean" It
    stock = input("Enter a stock quantity: ").lower().strip()