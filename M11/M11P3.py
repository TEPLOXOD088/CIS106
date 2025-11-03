
def salesrep(s):
    if s>100000:
        comm = s*0.10
    else:
        comm = s*0.05
    tgt = s*0.05
    return comm,tgt

again="yes"
while again.lower()=="yes":
    last=input("Last: ")
    s=float(input("Sales: "))
    comm,tgt=salesrep(s)
    print(last, comm, tgt)
    again=input("Run again (Yes or No)? ")
input("Press Enter to exit")
