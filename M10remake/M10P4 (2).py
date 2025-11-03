
def ticket(miles):
    if miles >= 30:
        return 12
    elif miles >= 20:
        return 10
    elif miles >= 10:
        return 8
    else:
        return 5

sum_tickets = 0

again = "yes"
while again.lower() == "yes":
    last = input("Enter last name: ")
    miles = int(input("Enter miles from downtown Chicago: "))
    price = ticket(miles)
    print("Ticket price:", price)
    sum_tickets += price

    again = input("Run again (Yes or No)? ")
print("Total of all tickets:", sum_tickets)
input("Press Enter to exit")
