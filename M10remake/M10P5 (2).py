
def assessed(county, market):
    county = county.lower()
    if county == "cook":
        pct = 0.90
    elif county == "dupage":
        pct = 0.80
    elif county == "mchenry":
        pct = 0.75
    elif county == "kane":
        pct = 0.60
    else:
        pct = 0.70

    return market * pct

sum_market = 0
sum_assessed = 0

again = "yes"
while again.lower() == "yes":
    county = input("Enter county: ")
    market = float(input("Enter market value: "))

    sum_market += market
    val = assessed(county, market)
    sum_assessed += val

    print("Assessed value:", round(val,2))
    again = input("Run again (Yes or No)? ")

print("Total market value:", round(sum_market,2))
print("Total assessed value:", round(sum_assessed,2))
input("Press Enter to exit")
