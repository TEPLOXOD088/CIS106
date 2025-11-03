
def op(a,b,c):
    c=c.lower()
    if c=="a":
        return a+b
    elif c=="s":
        return a-b
    elif c=="m":
        return a*b
    elif c=="d":
        if b==0:
            return -999
        else:
            return a/b
    return 0

again="yes"
while again.lower()=="yes":
    a=float(input("Num1: "))
    b=float(input("Num2: "))
    c=input("Op (A,S,M,D): ")
    result=op(a,b,c)
    print(a, b, c, result)
    if result==-999:
        print("Divide by zero attempt")
    again=input("Run again (Yes/No)? ")
input("Press Enter to exit")
