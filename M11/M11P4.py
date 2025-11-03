
def bowl(a,b,c,h):
    avg=(a+b+c)/3
    havg=avg+h
    return avg,havg

again="yes"
while again.lower()=="yes":
    last=input("Last: ")
    g1=float(input("Game1: "))
    g2=float(input("Game2: "))
    g3=float(input("Game3: "))
    h=float(input("Handicap: "))
    avg,havg=bowl(g1,g2,g3,h)
    print(last, avg, havg)
    again=input("Run again (Yes or No)? ")
input("Press Enter to exit")
