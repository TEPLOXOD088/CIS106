hours = float(input("Enter hours worked: "))
rate = float(input("Enter hourly rate: "))
if hours > 40:
    pay = 40 * rate + (hours - 40) * 1.5 * rate
else:
    pay = hours * rate
print("Total pay:", pay)