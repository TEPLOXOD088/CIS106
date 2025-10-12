principal = float(input("Enter principal amount: "))
rate = float(input("Enter interest rate: "))

balance = principal
total_interest = 0

print("Year  Beginning Balance  Ending Balance")
for year in range(1, 6):
    interest = balance * rate
    end_balance = balance + interest
    print(f"{year}     ${balance:,.2f}        ${end_balance:,.2f}")
    total_interest += interest
    balance = end_balance

print(f"Total interest earned: ${total_interest:,.2f}")
