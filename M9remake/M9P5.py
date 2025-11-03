
def tuition(cr,dc):
    dc=dc.lower()
    if dc=="i":
        return cr*250
    elif dc=="o":
        return cr*550
    return 0

again="yes"
sumt=0
while again.lower()=="yes":
    last=input("Last name: ")
    cr=float(input("Credit hours: "))
    dc=input("District code: ")
    t=tuition(cr,dc)
    print(last, t)
    sumt+=t
    again=input("Run again (Yes/No)? ")
print("Total tuition:", round(sumt,2))
input("Press Enter to exit")
