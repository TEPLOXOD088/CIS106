
def flip(st):
    if st.islower():
        return st.upper()
    else:
        return st.lower()

again="yes"
while again.lower()=="yes":
    s=input("String: ")
    print(s, flip(s))
    again=input("Run again (Yes/No)? ")
input("Press Enter to exit")
