def compute_gallons(length, width, height):
    # wall area: 2*(L*H) + 2*(W*H)
    area1 = length * height
    area2 = width * height
    total_area = 2 * area1 + 2 * area2
    gallons = total_area // 50
    if total_area % 50 != 0:
        gallons = gallons + 1
    return int(gallons)

def main():
    room_gallons = {}
    name = input("Enter room name (or DONE to finish): ")
    while name != "DONE":
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        height = float(input("Enter height: "))
        gallons = compute_gallons(length, width, height)
        room_gallons[name] = gallons
        name = input("Enter room name (or DONE to finish): ")

    print("Room\tGallons")
    print("----\t-------")
    for room, gallons in room_gallons.items():
        print(room + "\t" + str(gallons))

main()
