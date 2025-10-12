total_bonus = 0

with open("employees.txt") as file:
    lines = file.readlines()

for i in range(0, len(lines), 2):
    name = lines[i].strip()
    salary = float(lines[i+1].strip())
    if salary >= 100000:
        bonus = salary * 0.20
    elif salary >= 50000:
        bonus = salary * 0.15
    else:
        bonus = salary * 0.10
    total_bonus += bonus
    print(name, salary, bonus)

print("Total bonuses paid:", total_bonus)
