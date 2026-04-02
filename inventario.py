#Iteration in case the user inputs a wrong value
while True:
    #User data validation 
    try:
        #User data request 
        productName = input("Enter the product's name: ")
        productPrice = float(input("Enter the product's price: "))
        productQuantity = int(input("Enter the product's quantity: "))
        break
    except ValueError:
        #Error message for wrong user input
        print("Enter a valid value (E.g.Name = soap; price = 2.3; quantity = 2)")

#Mathematical operation for the total cost of the products
total_cost = productPrice * productQuantity
#Message for the user that shows their inputs and the total cost
print(f"Product: {productName} | Price: {productPrice} | Quantity: {productQuantity} | Total: {total_cost}")

# The program asks the user for a product name, price and quantity.
# It does a multiplication between the price and quantity to give
# the total cost for all of the items and show a brief summary 
# that contains the name, price, quantity and total cost of the products