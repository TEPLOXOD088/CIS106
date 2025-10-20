# Problem 3: Change string case

def change_case(user_string):
    if user_string.islower():
        new_string = user_string.upper()
    else:
        new_string = user_string.lower()
    print(f"Original string: {user_string}")
    print(f"New string: {new_string}")

# Example call
user_string = input("Enter a string: ")
change_case(user_string)
