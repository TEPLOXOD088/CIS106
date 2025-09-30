# M6P5 - Employee Bonus

last_name = input("Enter employee last name: ")
salary = float(input("Enter salary: "))
job_level = int(input("Enter job level: "))

if job_level >= 10:
    bonus_rate = 0.25
elif job_level >= 5:
    bonus_rate = 0.20
else:
    bonus_rate = 0.10

bonus = salary * bonus_rate

print(f"Employee: {last_name}")
print(f"Bonus:    {bonus:10.2f}")
