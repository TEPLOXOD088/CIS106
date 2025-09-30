# M6P2 - Part Cost

part = input("Enter part number: ")
quantity = int(input("Enter quantity: "))

if part == "10" or part == "55":
    unit_cost = 1.0
elif part == "99":
    unit_cost = 2.0
elif part == "80" or part == "70":
    unit_cost = 3.0
else:
    unit_cost = 5.0

total_cost = quantity * unit_cost

print(f"Part Number: {part}")
print(f"Cost per Unit: {unit_cost:10.2f}")
print(f"Total Cost:    {total_cost:10.2f}")
