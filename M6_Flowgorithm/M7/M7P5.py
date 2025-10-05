# M7P5 - Orders with discount calculation

total_discount = 0
choice = input("Do you want to enter an order? (Yes to continue): ").strip().lower()

while choice == "yes":
    qty = int(input("Enter quantity: "))
    price = float(input("Enter price per item: "))
    
    ext_price = qty * price
    if ext_price > 10000:
        discount_rate = 0.25
    else:
        discount_rate = 0.10
    
    discount = ext_price * discount_rate
    total = ext_price - discount
    
    print(f"Extended Price: ${ext_price:.2f}")
    print(f"Discount: ${discount:.2f}")
    print(f"Total: ${total:.2f}")
    
    total_discount += discount
    choice = input("Do you want to enter another order? (Yes to continue): ").strip().lower()

print(f"Total Discounts Given: ${total_discount:.2f}")
