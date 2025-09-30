# M6P1 - Widgets Pricing

quantity = int(input("Enter quantity of widgets: "))

if quantity > 10000:
    price = 10
elif quantity >= 5000:
    price = 20
else:
    price = 30

extended_price = quantity * price
tax = extended_price * 0.07
total = extended_price + tax

print(f"Extended Price: {extended_price:10.2f}")
print(f"Tax:            {tax:10.2f}")
print(f"Total:          {total:10.2f}")
