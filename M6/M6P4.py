# M6P4 - Concert Tickets

tickets = int(input("Enter number of tickets: "))

if tickets >= 25:
    price_per_ticket = 50
elif tickets >= 10:
    price_per_ticket = 60
elif tickets >= 5:
    price_per_ticket = 70
else:
    price_per_ticket = 75

total_cost = tickets * price_per_ticket

print(f"Tickets:         {tickets:10d}")
print(f"Price per Ticket:{price_per_ticket:10.2f}")
print(f"Total Cost:      {total_cost:10.2f}")
