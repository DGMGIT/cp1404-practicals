"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
CELSIUS = "c"
FAHRENHEIT = "f"


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = to_fahrenheit(celsius)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = to_celsius(fahrenheit)
            print(f"Result: {celsius:.2f}")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def to_fahrenheit(temperature):
    return temperature * 9.0 / 5 + 32


def to_celsius(temperature):
    return 5 / 9 * (temperature - 32)


if __name__ == "__main__":
    main()
