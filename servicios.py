#Add products
def add_product(inventory, product):
    """
    function that stores the information of the product in a dictionary and
    stores that dictionary in the inventory list
    """
    #Try block to validate the user's input
    try:
        #Data entry of the product
        productName = input("Enter the product's name: ").lower()
        productPrice = float(input(f"Enter the {productName.capitalize()} price: "))
        productQuantity = int(input(f"Enter the {productName.capitalize()} quantity: "))
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

#Show inventory
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
            print(f"Name: {productInv["name"].capitalize()} | Price: {productInv["price"]} | Quantity: {productInv["quantity"]}") #Message showing the product


#Search product
def search_product(inventory, productName):
    """
    iterates the inventory list to search for a product. If the product is found the functions displays the product's values,
    if not found the function tells the user the product is not in inventory
    """
    inInventory = False
    for product in inventory:
        if product["name"] == productName:
            return product
    return None

#Update product
def update_product(inventory, productName, productNewPrice, productNewQuantity):
    """
    Iterates the inventory searching for a product to update. If the product is found the function updates the product's value, if not found the
    function tells the user the product is not in inventory
    """
    inInventory = False
    for product in inventory:
        if product["name"] == productName:
            product.update({"price": productNewPrice})
            product.update({"quantity": productNewQuantity})
            inInventory = True
    if inInventory == False:
        print("The product is not in inventory")
    else:
        print("Sucesfully updated")

#Delete product
def delete_product(inventory, productName):
    """
    Iterates the inventory searching for a product to erase. If the product is found the function erases the dict containing all of the
    product's values, If not found the function tells the user the product is not in inventory
    """
    inInventory = False
    for idx, product in enumerate(inventory):
        if product["name"] == productName:
            inInventory = True
            inventory.pop(idx)
            print("Product deleted")
    if inInventory == False:
        print("The product is not in inventory")

#Calculate Statistics
def calculate_statistics(inventory):
    """
    This functions calculates:
    Total Units
    Total Value
    Most Expensive Product
    Highest Stocked Product    
    """
    totalUnits = 0
    totalValue = 0
    mostExpensive = inventory[0]
    highestStock = inventory[0]
    subtotal = (lambda p: p["price"] * p["quantity"])

    #Validation if the inventory is empty
    if not inventory:
        print("\nThe inventory is empty, there's nothing to calculate") #Message for the user to notice the inventory is empty, so no calculation can be done
    else:
        for product in inventory:
            totalUnits += product.get("quantity")
            totalValue += subtotal(product)

            if product.get("price") > mostExpensive.get("price"):
                mostExpensive = product
            
            if product.get("quantity") > highestStock.get("quantity"):
                highestStock = product

        print(f"Total Units: {totalUnits}")
        print(f"Total Value: {totalValue}")
        print(f"Most Expensive Product: {mostExpensive.get("name")} | $ {mostExpensive.get("price")}")
        print(f"Highest Stocked Product: {highestStock.get("name")} | {highestStock.get("quantity")} Units")

