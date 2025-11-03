
def compute(q,p,d):
    disc = q*p*d
    dp = q*p - disc
    return disc, dp

again="yes"
while again.lower()=="yes":
    q=float(input("Qty: "))
    p=float(input("Price: "))
    d=float(input("Disc rate: "))
    disc, dp = compute(q,p,d)
    print(q,p,disc,dp)
    again=input("Run again (Yes or No)? ")
input("Press Enter to exit")
