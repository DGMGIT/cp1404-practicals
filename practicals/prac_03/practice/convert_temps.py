OUTPUT_FILE_NAME = "temps_output.txt"
FAHRENHEIT = 'f'
CELSIUS = 'c'


def main():
    file_name = input("Enter the temps file name: ")
    file = open(file_name, 'r')
    output_file = open(OUTPUT_FILE_NAME, 'w')
    conversion_choice = input("What would you like to convert to: ").lower()
    for line in file.readlines():
        line = line.strip()
        try:
            temp = int(line)
            if conversion_choice == CELSIUS:
                print(f"{to_celsius(temp):.2f}", file=output_file)
            elif conversion_choice == FAHRENHEIT:
                print(f"{to_fahrenheit(temp):.2f}", file=output_file)
        except ValueError as e:
            print(e)
            return

    file.close()
    output_file.close()


def to_fahrenheit(temperature):
    return temperature * 9.0 / 5 + 32


def to_celsius(temperature):
    return 5 / 9 * (temperature - 32)


if __name__ == "__main__":
    main()
