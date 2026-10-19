"""Mini-project solution – Unit Converter."""


def km_to_miles(km):
    return km * 0.621371


def miles_to_km(miles):
    return miles / 0.621371


def kg_to_pounds(kg):
    return kg * 2.20462


def pounds_to_kg(lb):
    return lb / 2.20462


def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32


def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9


CONVERSIONS = {
    "1": ("km → miles", km_to_miles),
    "2": ("miles → km", miles_to_km),
    "3": ("kg → pounds", kg_to_pounds),
    "4": ("pounds → kg", pounds_to_kg),
    "5": ("°C → °F", celsius_to_fahrenheit),
    "6": ("°F → °C", fahrenheit_to_celsius),
}


def show_menu():
    print("\n🔁 UNIT CONVERTER")
    for key, (label, _) in CONVERSIONS.items():
        print(f"{key}. {label}")
    print("q. Quit")


def main():
    while True:
        show_menu()
        choice = input("Choose: ").strip().lower()
        if choice == "q":
            print("Bye!")
            break
        if choice not in CONVERSIONS:
            print("Invalid choice.")
            continue
        label, convert = CONVERSIONS[choice]
        value = float(input("Value: "))
        print(f"{label}: {value} → {convert(value):.2f}")


if __name__ == "__main__":
    main()
