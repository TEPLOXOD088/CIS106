
def mpg(m,g):
    if g==0:
        return 0
    return m/g

again="yes"
count=0
while again.lower()=="yes":
    city=input("Destination: ")
    m=float(input("Miles: "))
    g=float(input("Gallons: "))
    calc=mpg(m,g)
    print(city, m, calc)
    count+=1
    again=input("Run again (Yes/No)? ")
print("Trips:", count)
input("Press Enter to exit")
