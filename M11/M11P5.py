
total=0
tax=0

def compute(q,p):
    global total,tax
    total=q*p
    tax=total*0.07

again="yes"
while again.lower()=="yes":
    q=float(input("Qty: "))
    p=float(input("UnitPrice: "))
    compute(q,p)
    print(total, tax)
    again=input("Run again (Yes or No)? ")
input("Press Enter to exit")
