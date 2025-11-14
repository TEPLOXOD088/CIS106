def main():
    names=[]
    scores=[]
    count=int(input("How many students? "))
    for i in range(count):
        n=input("Enter last name: ")
        s=int(input("Enter score: "))
        names.append(n)
        scores.append(s)

    high_val=scores[0]
    high_idx=0
    low_val=scores[0]
    low_idx=0

    for i in range(1,len(scores)):
        if scores[i] > high_val:
            high_val=scores[i]
            high_idx=i
        if scores[i] < low_val:
            low_val=scores[i]
            low_idx=i

    print(names[high_idx], high_val)
    print(names[low_idx], low_val)

main()
