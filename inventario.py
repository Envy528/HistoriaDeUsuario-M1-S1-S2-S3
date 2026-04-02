inventory = [] 
product = {}
option = None
while option != "4":
    option = input("\n1. Add Product\n2. Show Inventory\n3. Calculate statistics\n4. Exit\nYour Option: ")

    if option == "1":
        print("\nYou chose to add a product (option 1)\n")
        productName = input("Enter the product's name:  ")
        productPrice = float(input(f"Enter the {productName} price: "))
        productQuantity = int(input(f"Enter the {productName} quantity: "))
        print("\nProduct sucessfuly added!")

        product = {
            "name": productName,
            "price": productPrice,
            "quantity": productQuantity
        }

        inventory.append(product)
    
    elif option == "2":
        print("\nYou chose to show the inventory (option 2)")
        if not inventory:
            print("\nThe inventory is empty")
        else:
            for idx, productInv in enumerate(inventory):
                print(f"\nProduct {idx+1}:")
                print(f"Name: {productInv["name"]} | Price: {productInv["price"]} | Quantity: {productInv["quantity"]}")

    elif option == "3":
        print("calculate") #testing
    elif option == "4":
        print("leave") #testing
    else:
        print("Invalid input, try again with one of the options (1-4)")