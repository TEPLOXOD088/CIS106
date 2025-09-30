# M6P3 - CD Interest

principle = float(input("Enter principle amount: "))
years = int(input("Enter years to maturity: "))

if principle > 100000 and years == 5:
    rate = 0.06
elif 50000 <= principle <= 100000 and years == 10:
    rate = 0.05
elif 50000 <= principle <= 100000 and years == 5:
    rate = 0.04
else:
    rate = 0.02

interest = principle * rate

print(f"Principle:     {principle:10.2f}")
print(f"Interest Rate: {rate*100:10.2f}%")
print(f"First Year Interest: {interest:10.2f}")
