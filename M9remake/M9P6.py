
def rewards(pts,c):
    c=c.lower()
    if c=="c":
        return pts*2
    elif c=="x":
        return pts*3
    else:
        return pts*1.5

again="yes"
while again.lower()=="yes":
    pts=float(input("Points: "))
    c=input("Code: ")
    r=rewards(pts,c)
    print(pts, c, r)
    again=input("Run again (Yes/No)? ")
input("Press Enter to exit")
