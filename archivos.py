def save_csv(inventory, path, includeHeader = True):
    """
    Writes the current inventory to a CSV file at the given path.

    """
    if not inventory:
        print("The inventory is empty")
    
    try:
        with open(path, "w") as file:
            if includeHeader:
                file.write("name,price,quantity\n")
            
            for product in inventory:
                file.write(f"{product.get("name")},{product.get("price")},{product.get("quantity")}\n")

        print(f"Inventory saved in: {path}")

    
    except Exception as e:
        print(f"Error saving file: {e}")