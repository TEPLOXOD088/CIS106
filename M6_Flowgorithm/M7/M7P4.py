# M7P4 - Employee pay with overtime

count = 0
total_pay = 0
choice = input("Do you want to enter employee data? (Yes to continue): ").strip().lower()

while choice == "yes":
    last_name = input("Enter employee last name: ")
    hours = float(input("Enter hours worked: "))
    rate = float(input("Enter rate of pay: "))
    
    if hours > 40:
        gross = 40 * rate + (hours - 40) * rate * 1.5
    else:
        gross = hours * rate
    
    print(f"Employee: {last_name}, Gross Pay: ${gross:.2f}")
    total_pay += gross
    count += 1
    
    choice = input("Do you want to enter another employee? (Yes to continue): ").strip().lower()

if count > 0:
    avg_pay = total_pay / count
    print(f"Total Employees: {count}")
    print(f"Total Gross Pay: ${total_pay:.2f}")
    print(f"Average Pay: ${avg_pay:.2f}")
else:
    print("No employees entered.")
