# M4P3 - Meal tip calculator

# Input
meal_total = float(input("Enter total for meal: "))

# Processing + Output
for tip_percent in [0.15, 0.18, 0.20]:
    tip = meal_total * tip_percent
    total_with_tip = meal_total + tip
    
    print(f"With {int(tip_percent*100)}% Tip:")
    print("Total:", format(meal_total, ".2f"))
    print("Tip:", format(tip, ".2f"))
    print("Total with Tip", format(total_with_tip, ".2f"))
    print()
