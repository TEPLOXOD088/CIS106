
def batavg(h,a):
    if a==0:
        return 0
    return h/a

again="yes"
count=0
while again.lower()=="yes":
    last=input("Last name: ")
    h= float(input("Hits: "))
    a= float(input("AtBats: "))
    avg=batavg(h,a)
    print(last, avg)
    count+=1
    again=input("Run again (Yes/No)? ")
print("Players:", count)
input("Press Enter to exit")
