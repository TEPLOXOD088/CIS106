# Module 14 - Problem 2
# Student class with tuition calculation using if/else

class Student:
    def __init__(self, first_name, last_name, district_code, enrolled_credits):
        self.first_name = first_name
        self.last_name = last_name
        self.district_code = district_code.upper()
        self.enrolled_credits = enrolled_credits

    def compute_tuition(self):
        """Compute tuition based on district code and enrolled credits."""
        if self.district_code == "I":       # in-district
            rate = 250.0
        else:                                # out-of-district (anything not I)
            rate = 500.0
        return self.enrolled_credits * rate

    def __str__(self):
        return (f"{self.first_name} {self.last_name} "
                f"(District {self.district_code}, Credits: {self.enrolled_credits})")


def main():
    print("=== Student Tuition Calculator (if/else) ===")
    first = input("Enter student first name: ")
    last = input("Enter student last name: ")
    district = input("Enter district code (I for in-district, anything else for out-of-district): ")
    credits = int(input("Enter number of enrolled credits: "))

    student = Student(first, last, district, credits)
    tuition = student.compute_tuition()

    print()
    print(student)
    print(f"Tuition owed: ${tuition:,.2f}")


if __name__ == "__main__":
    main()
