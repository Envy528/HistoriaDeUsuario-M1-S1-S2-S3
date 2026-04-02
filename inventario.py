def add_product(inventory, product):
    """
    function that stores the information of the product in a dictionary and
    stores that dictionary in the inventory list
    """
    #Try block to validate the user's input
    try:
        #Data entry of the product
        productName = input("Enter the product's name:  ")
        productPrice = float(input(f"Enter the {productName} price: "))
        productQuantity = int(input(f"Enter the {productName} quantity: "))
        print("\nProduct sucessfuly added!")
        #Storing the data
        product = { #Dictionary
            "name": productName,
            "price": productPrice,
            "quantity": productQuantity
        }
        inventory.append(product) #List

    #Message in case the user inputs an invalid value
    except ValueError:
        print(f"\n{"-"*20}ERROR{"-"*20}\nEnter a valid value in price and quantity (e.g. Price = 25.5; Quantity = 2)\nTry Again.")
    
def show_inventory(inventory):
    """
    function that goes through the inventory list to show it's contents in a simple user friendly way
    """
    #Validation if the inventory is empty
    if not inventory:
        print("\nThe inventory is empty")#Message for the user to notice the inventory is empty
    else:
        #For that goes through the inventory to acces the products
        for idx, productInv in enumerate(inventory):
            print(f"\nProduct {idx+1}:") #The number of the product 
            print(f"Name: {productInv["name"]} | Price: {productInv["price"]} | Quantity: {productInv["quantity"]}") #Message showing the product


def calculate_statistics(inventory, totalInventory):
    """
    function that calculates the inventory total value and the total products registered in it
    """
    #Validation if the inventory is empty
    if not inventory:
        print("\nThe inventory is empty, there's nothing to calculate") #Message for the user to notice the inventory is empty, so no calculation can be done
    else:
        #Accesing the inventory looking for the products
        for productInv in inventory:
            totalProduct = productInv["price"] * productInv["quantity"] #Calculating the total individual product value by multiplicating it's price for it's quantity
            totalInventory += totalProduct #Adding all the totals individual prices of the products to store the inventory's value
        print(f"\nTotal value in inventory: {totalInventory}\nTotal Products Registered: {len(inventory)}") #MEssage showing the calculations


#Initialize variables 
inventory = [] 
product = {}
option = None
totalProduct = 0
totalInventory = 0

#Menu
while option != "4": #While to iterate until the user decides to leave
    option = input("\n1. Add Product\n2. Show Inventory\n3. Calculate statistics\n4. Exit\nYour Option: ") #Menu message
    #Add product
    if option == "1":
        print("\nYou chose to add a product (option 1)\n") #Showing the user the option they selected
        add_product(inventory, product) #calling the add product function
    elif option == "2":
        print("\nYou chose to show the inventory (option 2)") #Showing the user the option they selected
        show_inventory(inventory) #calling the show inventory function

    elif option == "3":
        print("\nYou chose to calculate the inventory statistics (option 3)") #Showing the user the option they selected
        calculate_statistics(inventory, totalInventory) #calling the calculate statistics function
    elif option == "4":
        print("\nGoodbye!!") #Exit message
    #Validation in case the user inputs a wrong option
    else:
        print("Invalid input, try again with one of the options (1-4)") #Message for a wrong user's input


#The week's objetive is to make a program that can manage numerous products in an inventory,
#the program must have features to add products, show the products in inventory and calculate
#it's total value and total products registered while validating any error that the program can have