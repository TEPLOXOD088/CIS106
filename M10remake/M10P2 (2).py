
def wall_sqft(length, width, height):
    return (2 * length * height) + (2 * width * height)

def ceiling_floor_area(length, width):
    return length * width

again = "yes"
while again.lower() == "yes":
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    height = float(input("Enter height: "))

    sqft = wall_sqft(length, width, height)
    gallons = sqft / 50
    print("Gallons needed for walls:", round(gallons, 2))

    # Bonus ceiling/floor
    area = ceiling_floor_area(length, width)
    bonus_gallons = area / 50
    print("Gallons needed for ceiling/floor:", round(bonus_gallons, 2))

    again = input("Run again (Yes or No)? ")
input("Press Enter to exit")
