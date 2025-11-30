# Module 14 - Problem 1
# Employee class with bonus method

class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def compute_bonus(self, bonus_rate):
        """Return the bonus based on bonus_rate * salary."""
        return self.salary * bonus_rate

    def __str__(self):
        return f"{self.first_name} {self.last_name}, Salary: ${self.salary:,.2f}"


def main():
    print("=== Employee Bonus Calculator ===")
    first = input("Enter employee first name: ")
    last = input("Enter employee last name: ")
    salary = float(input("Enter employee annual salary: "))

    emp = Employee(first, last, salary)
    print(emp)

    rate = float(input("Enter bonus rate (for 5% enter 0.05): "))
    bonus = emp.compute_bonus(rate)
    print(f"Bonus for {emp.first_name} {emp.last_name}: ${bonus:,.2f}")


if __name__ == "__main__":
    main()
