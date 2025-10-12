total = 0
count = 0

with open("items.txt") as file:
    lines = file.readlines()

for i in range(0, len(lines), 3):
    item = lines[i].strip()
    qty = int(lines[i+1].strip())
    price = float(lines[i+2].strip())
    extended = qty * price
    total += extended
    count += 1
    print(item, qty, price, extended)

print("Total of orders:", total)
print("Number of orders:", count)
print("Average order:", total / count)
