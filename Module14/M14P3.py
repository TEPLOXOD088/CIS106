# Module 14 - Problem 3
# Student tuition using a district-rate dictionary

# District code to rate dictionary
DISTRICT_RATES = {
    "I": 250.0,  # in-district
    "O": 500.0,  # out-of-district
    "X": 800.0,  # international
    "G": 250.0   # reciprocity (same as in-district)
}

DEFAULT_RATE = 500.0  # any code not listed treated as out-of-district


class Student:
    def __init__(self, first_name, last_name, district_code, enrolled_credits):
        self.first_name = first_name
        self.last_name = last_name
        self.district_code = district_code.upper()
        self.enrolled_credits = enrolled_credits

    def compute_tuition(self):
        """Compute tuition based on district code using DISTRICT_RATES dict."""
        rate = DISTRICT_RATES.get(self.district_code, DEFAULT_RATE)
        return self.enrolled_credits * rate

    def __str__(self):
        return (f"{self.first_name} {self.last_name} "
                f"(District {self.district_code}, Credits: {self.enrolled_credits})")


def main():
    print("=== Student Tuition Calculator (dictionary) ===")
    # Instantiate at least one student of each district code: I, O, X, G
    students = [
        Student("Ingrid", "InDistrict", "I", 12),
        Student("Oscar", "OutDistrict", "O", 9),
        Student("Xavier", "International", "X", 15),
        Student("Grace", "Reciprocity", "G", 6),
    ]

    for s in students:
        tuition = s.compute_tuition()
        print(s)
        print(f"Tuition owed: ${tuition:,.2f}")
        print("-" * 40)


if __name__ == "__main__":
    main()
