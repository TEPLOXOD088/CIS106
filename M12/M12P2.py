def display_forward(names, scores):
    for i in range(len(names)):
        print(names[i], scores[i])

def display_reverse(names, scores):
    for i in range(len(names)-1, -1, -1):
        print(names[i], scores[i])

def main():
    names = ["Smith","Johnson","Williams","Brown","Jones",
             "Garcia","Miller","Davis","Rodriguez","Martinez"]
    scores=[]
    for i in range(len(names)):
        s=int(input("Enter score for "+names[i]+": "))
        scores.append(s)
    display_forward(names, scores)
    display_reverse(names, scores)

main()
