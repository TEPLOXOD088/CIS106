year = int(input("Enter birth year: "))
month = int(input("Enter birth month: "))
current_year = 2025
current_month = 10
age = current_year - year
if current_month < month:
    age -= 1
print("Your age is:", age)