# Module 15 - Problem 2
# Car class and Sportcar derived class with options

class Car:
    def __init__(self, make, model, sticker_price):
        self.make = make
        self.model = model
        self.sticker_price = sticker_price

    def discount_price(self):
        """Return 90% of sticker price."""
        return self.sticker_price * 0.90

    def __str__(self):
        return f"Car: {self.make} {self.model}, Sticker Price: ${self.sticker_price:,.2f}"


class Sportcar(Car):
    SPORT_WHEELS_PRICE = 1000.00
    SPORT_ENGINE_PRICE = 3000.00
    SPORT_INTERIOR_PRICE = 2000.00

    def __init__(self, make, model, sticker_price):
        super().__init__(make, model, sticker_price)
        # option flags (Y/N)
        self._sport_wheels = "N"
        self._sport_engine = "N"
        self._sport_interior = "N"

    # Option methods
    def SportWheels(self, choice):
        """Set SportWheels option to 'Y' or 'N'."""
        self._sport_wheels = choice.upper()

    def SportEngine(self, choice):
        """Set SportEngine option to 'Y' or 'N'."""
        self._sport_engine = choice.upper()

    def SportInterior(self, choice):
        """Set SportInterior option to 'Y' or 'N'."""
        self._sport_interior = choice.upper()

    def updated_price(self):
        """Return discounted price plus any selected sport options."""
        price = self.discount_price()

        if self._sport_wheels == "Y":
            price += self.SPORT_WHEELS_PRICE
        if self._sport_engine == "Y":
            price += self.SPORT_ENGINE_PRICE
        if self._sport_interior == "Y":
            price += self.SPORT_INTERIOR_PRICE

        return price

    def __str__(self):
        return (f"Sportcar: {self.make} {self.model}, Sticker Price: ${self.sticker_price:,.2f}, "
                f"Options(Wheels={self._sport_wheels}, Engine={self._sport_engine}, "
                f"Interior={self._sport_interior})")


def main():
    print("=== Module 15 - Problem 2: Car and Sportcar Inheritance ===\n")

    # Two regular cars
    car1 = Car("Toyota", "Camry", 30000)
    car2 = Car("Honda", "Civic", 25000)

    print(car1)
    print(f"  Discount price (90% of sticker): ${car1.discount_price():,.2f}")
    print("-" * 60)
    print(car2)
    print(f"  Discount price (90% of sticker): ${car2.discount_price():,.2f}")
    print("=" * 60)

    # Two sportcars to show combinations of options
    sport1 = Sportcar("Ford", "Mustang", 40000)
    # All options ON
    sport1.SportWheels("Y")
    sport1.SportEngine("Y")
    sport1.SportInterior("Y")

    sport2 = Sportcar("Chevrolet", "Corvette", 60000)
    # Mix of options: only engine and wheels
    sport2.SportWheels("Y")
    sport2.SportEngine("Y")
    sport2.SportInterior("N")

    # Show all combinations example: base (no options), some options, all options
    sport_base = Sportcar("Subaru", "BRZ", 32000)  # all N by default
    sport_some = Sportcar("Mazda", "MX-5", 31000)
    sport_some.SportWheels("Y")  # only wheels

    sportcars = [sport_base, sport_some, sport1, sport2]

    for s in sportcars:
        print(s)
        print(f"  Discount price (no options added yet): ${s.discount_price():,.2f}")
        print(f"  Updated price with selected options: ${s.updated_price():,.2f}")
        print("-" * 60)


if __name__ == "__main__":
    main()
