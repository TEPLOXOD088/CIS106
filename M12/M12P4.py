def display_all(names, avgs):
    for i in range(len(names)):
        print(names[i], avgs[i])

def main():
    names=[]
    avgs=[]
    for i in range(10):
        n=input("Enter player name: ")
        a=float(input("Enter batting avg: "))
        names.append(n)
        avgs.append(a)

    display_all(names, avgs)

    find=input("Search name (QUIT to exit): ")
    while find!="QUIT":
        for i in range(len(names)):
            if names[i]==find:
                print(names[i], avgs[i])
        find=input("Search name (QUIT to exit): ")

main()
