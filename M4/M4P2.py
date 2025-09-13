# M4P2 - Stock value change

# Input
purchase_price = float(input("Enter purchase price per share: "))
current_price = float(input("Enter current stock price: "))
quantity = int(input("Enter quantity of stock: "))

# Processing
value = (current_price - purchase_price) * quantity

# Output
print("Change in stock value:", format(value, ".2f"))
