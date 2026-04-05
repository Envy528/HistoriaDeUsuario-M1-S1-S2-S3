def save_csv(inventory, fileName, includeHeader = True):
    """
    Writes the current inventory to a CSV file at the given file Name.

    """
    #In case the inventory is empty
    if not inventory:
        print("The inventory is empty")
    
    try:
        #Writing the data in the csv file
        with open(fileName, "w") as file:
            if includeHeader:
                file.write("name,price,quantity\n")
            
            for product in inventory:
                file.write(f"{product.get("name")},{product.get("price")},{product.get("quantity")}\n")

        print(f"Inventory saved in: {fileName}")

    
    except Exception as e:
        print(f"Error saving file: {e}")


def load_csv(fileName):
    """
    Reads a CSV file and returns its contents as a list of product dictionaries.
    """

    inventory = []
    invalidRows = 0

    try:
        #Read file
        with open(fileName, "r") as file:
            lines = file.readlines()

        #validate header
        if lines[0].strip() != "name,price,quantity":
            print("Invalid file format")
            return [], 0


        for line in lines[1:]:
            parts = line.strip().split(",")
            
            #Validates the column length
            if len(parts) != 3:
                invalidRows += 1
                continue

            name, price, quantity = parts

            try:
                price = float(price)
                quantity = int(quantity)

                #Validates if the number is negative
                if price < 0 or quantity < 0:
                    invalidRows += 1
                    continue

                inventory.append({
                    "name": name,
                    "price": price,
                    "quantity": quantity
                })

            except ValueError:
                invalidRows += 1 
            
        return inventory, invalidRows
    
    except FileNotFoundError:
        print("File not found")
        return [], 0
    
    except UnicodeDecodeError:
        print("File encoding error")
        return [], 0
    
    except Exception as e:
        print(f"Error loading file: {e}")
        return [], 0