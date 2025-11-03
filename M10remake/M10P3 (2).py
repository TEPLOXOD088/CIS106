
def sale_price(msrp, make, model, ev):
    make = make.lower()
    model = model.lower()
    ev = ev.lower()

    if make == "honda" and model == "accord":
        discount = 0.10
    elif make == "toyota" and model == "rav4":
        discount = 0.15
    elif ev == "y":
        discount = 0.30
    else:
        discount = 0.05

    new_price = msrp * (1 - discount)
    total = new_price * 1.07
    return total

sum_msrp = 0
sum_sales = 0

again = "yes"
while again.lower() == "yes":
    make = input("Enter make: ")
    model = input("Enter model: ")
    ev = input("Electric vehicle (Y/N)? ")
    msrp = float(input("Enter MSRP: "))
    sum_msrp += msrp

    total = sale_price(msrp, make, model, ev)
    sum_sales += total
    print("Final sale price:", round(total, 2))

    again = input("Run again (Yes or No)? ")

print("Sum MSRP:", round(sum_msrp,2))
print("Sum Sales:", round(sum_sales,2))
input("Press Enter to exit")
