def display_forward(names):
    for i in range(len(names)):
        print(names[i])

def display_reverse(names):
    for i in range(len(names)-1, -1, -1):
        print(names[i])

def main():
    last_names = ["Smith","Johnson","Williams","Brown","Jones",
                  "Garcia","Miller","Davis","Rodriguez","Martinez"]
    display_forward(last_names)
    display_reverse(last_names)

main()
