# Module 15 - Problem 1
# Classes, Objects, and Inheritance
# Employee (base class) and Manager (derived class)

class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def compute_bonus(self, bonus_rate):
        """Return a bonus based on bonus_rate * salary."""
        return self.salary * bonus_rate

    def __str__(self):
        return f"Employee: {self.first_name} {self.last_name}, Salary: ${self.salary:,.2f}"


class Manager(Employee):
    def long_term_bonus(self):
        """Long-term bonus is 40% (0.40) of manager salary."""
        return self.salary * 0.40

    def __str__(self):
        return f"Manager: {self.first_name} {self.last_name}, Salary: ${self.salary:,.2f}"


def main():
    print("=== Module 15 - Problem 1: Employee and Manager Inheritance ===\n")

    # Two regular employees
    emp1 = Employee("Alex", "Worker", 50000)
    emp2 = Employee("Jamie", "Staff", 60000)

    # Two managers
    mgr1 = Manager("Morgan", "Boss", 90000)
    mgr2 = Manager("Taylor", "Lead", 110000)

    employees = [emp1, emp2, mgr1, mgr2]

    for person in employees:
        print(person)
        # Show normal bonus example (10%)
        bonus = person.compute_bonus(0.10)
        print(f"  10% annual bonus: ${bonus:,.2f}")

        # If this is a Manager, also show long-term bonus
        if isinstance(person, Manager):
            lt_bonus = person.long_term_bonus()
            print(f"  Long-term bonus (40% of salary): ${lt_bonus:,.2f}")
        print("-" * 50)


if __name__ == "__main__":
    main()
