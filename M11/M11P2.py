
def scores(a,b,c):
    total = a+b+c
    avg = total/3
    return total, avg

again="yes"
while again.lower()=="yes":
    last=input("Last: ")
    a=float(input("Exam1: "))
    b=float(input("Exam2: "))
    c=float(input("Exam3: "))
    tot,avg=scores(a,b,c)
    print(last, tot, avg)
    again=input("Run again (Yes or No)? ")
input("Press Enter to exit")
