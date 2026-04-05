from servicios import *    
from archivos import *
#Initialize variables 
inventory = [] 
product = {}
option = None
totalProduct = 0
totalInventory = 0

#Menu
while option != "9": #While to iterate until the user decides to leave
    option = input("\n1. Add Product\n2. Show Inventory\n3. Search Product\n4. Update Product\n5. Delete Product\n6. Calculate Statistics\n7. Save CSV\n8. Load CSV\n9. Exit\nYour Option: ") #Menu message
    #Add product
    if option == "1":
        print("\nYou chose to add a product (option 1)\n") #Showing the user the option they selected
        add_product(inventory, product) #calling the add product function
    elif option == "2":
        print("\nYou chose to show the inventory (option 2)") #Showing the user the option they selected
        show_inventory(inventory) #calling the show inventory function

    elif option == "3":
        print("\nYou chose to search for a product (option 3)") #Showing the user the option they selected
        productName = input("Enter the product's name you are looking for: ").lower() #Ask the product's name that the user wants
        product = search_product(inventory, productName)
        print(f"Product: {product.get("name").capitalize()}\nPrice: $ {product.get("price")} | {product.get("quantity")} units")
    elif option == "4":
        print("\nYou chose to update a product (option 4)") #Showing the user the option they selected
        try:
            productName = input("Enter the product's name you want to update: ").lower() #Ask the product's name that the user wants
            productPrice = float(input("Enter the new price of the product: ")) #The new price to update
            productQuantity = int(input("Enter the new quantity of the product: ")) #The new quantity to update
            update_product(inventory, productName, productPrice, productQuantity)
        except:
            print(f"\n{"-"*20}ERROR{"-"*20}\nEnter a valid value in price and quantity (e.g. Price = 25.5; Quantity = 2)\nTry Again.")
    elif option == "5":
        print("\nYou chose to delete a product (option 5)") #Showing the user the option they selected
        productName = input("Enter the product's name you want to update: ").lower() #Ask the product's name that the user wants
        delete_product(inventory, productName)
    elif option == "6":
        print("\nYou chose to calculate inventory statistics (option 6)") #Showing the user the option they selected
        calculate_statistics(inventory)
    elif option == "7":
        print("\nYou chose to save the CSV (option 7)") #Showing the user the option they selected
        fileName = input("File Name and the extension (I.g: Example.csv)\nFile Name: ")
        save_csv(inventory, fileName)
    elif option == "8":
        print("\nYou chose to load the CSV (option 8)") #Showing the user the option they selected
        fileName = input("File Name and the extension (I.g: Example.csv)\nFile Name: ")
        newData, errors = load_csv(fileName)

        if len(newData) > 0:
            csvOption = input("Overwrite inventory? (Y/N): ")

            if csvOption.upper() == "Y":
                inventory = newData
                action = "replaced"
            elif csvOption.upper() == "N":
                #Merge Inventories
                for newProduct in newData:
                    existing = search_product(inventory, newProduct["name"])

                    if existing:
                        existing["quantity"] += newProduct["quantity"]
                        if existing["price"] != newProduct["price"]:
                            existing["price"] = newProduct["price"]
                    else:
                        inventory.append(newProduct)
                action = "merged"
            else:
                print("Invalid choice, the inventory was not modified")
                action = "not modified"
            
            print(f"Loaded: {len(newData)} products")
            print(f"Invalid rows: {errors}")
            print(f"Inventory {action}")
        else:
            print("No valid data loaded")


    elif option == "9":
        print("You selected to exit the program\nGoodbye!!!") #End the program

    #Validation in case the user inputs a wrong option
    else:
        print("Invalid input, try again with one of the options (1-4)") #Message for a wrong user's input