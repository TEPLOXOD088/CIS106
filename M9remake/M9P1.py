
def extended_price(q,p):
    total = q*p
    if total > 10000:
        total = total*0.9
    return total

again="yes"
sumext=0
while again.lower()=="yes":
    qty = float(input("Enter quantity: "))
    price= float(input("Enter unit price: "))
    ext=extended_price(qty,price)
    sumext+=ext
    print(qty, price, ext)
    again=input("Run again (Yes/No)? ")
print("Total extended:", round(sumext,2))
input("Press Enter to exit")
