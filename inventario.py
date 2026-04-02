
while True:
    try:
        productName = input("Enter the product's name: ")
        productPrice = float(input("Enter the product's price: "))
        productQuantity = int(input("Enter the product's quantity: "))
        break
    except ValueError:
        print("Enter a valid value (E.g.Name = soap; price = 2.3; quantity = 2)")

total_cost = productPrice * productQuantity