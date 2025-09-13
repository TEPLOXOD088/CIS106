# M4P5 - Break-even calculator

# Input
fixed_costs = float(input("Enter fixed costs: "))
price_per_unit = float(input("Enter price per unit: "))
cost_per_unit = float(input("Enter cost per unit: "))

# Processing
break_even = fixed_costs / (price_per_unit - cost_per_unit)

# Output
print("Break-even point (units):", format(break_even, ".2f"))
