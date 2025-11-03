
def forecast(month, sales):
    month = month.lower()
    if month in ["jan", "feb", "mar"]:
        percent = 0.10
    elif month in ["apr", "may", "jun"]:
        percent = 0.15
    elif month in ["jul", "aug", "sep"]:
        percent = 0.20
    elif month in ["oct", "nov", "dec"]:
        percent = 0.25
    else:
        percent = 0

    next_month_sales = sales * (1 + percent)
    return next_month_sales

again = "yes"
while again.lower() == "yes":
    last = input("Enter last name: ")
    month = input("Enter month abbreviation (Jan, Feb, etc): ")
    sales = float(input("Enter sales: "))
    result = forecast(month, sales)
    print("Next month's forecasted sales:", round(result, 2))
    again = input("Run again (Yes or No)? ")
input("Press Enter to exit")
