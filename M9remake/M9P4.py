
def rate(code):
    code=code.lower()
    if code=="l":
        return 25
    elif code=="a":
        return 30
    elif code=="j":
        return 50
    return 0

again="yes"
sumgross=0
while again.lower()=="yes":
    last=input("Last name: ")
    code=input("Job code: ")
    hrs=float(input("Hours: "))
    r=rate(code)
    if hrs>40:
        gross=40*r+(hrs-40)*r*1.5
    else:
        gross=hrs*r
    print(last, gross)
    sumgross+=gross
    again=input("Run again (Yes/No)? ")
print("Total gross:", round(sumgross,2))
input("Press Enter to exit")
