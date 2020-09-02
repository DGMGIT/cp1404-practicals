LOWER = 33
UPPER = 127


def main():
    char = input("Enter a character: ")
    print("The ASCII code for {} is {}".format(char, ord(char)))

    ascii_code = get_number(LOWER, UPPER)
    print("The character for {} is {}".format(ascii_code, chr(ascii_code)))
    columns = int(input("How many columns: "))
    count = 0
    for i in range(LOWER, UPPER + 1):
        if count != 0 and count % columns == 0:
            count = 0
            print()
        print("{:>3} {}".format(i, chr(i)), end="\t")
        count += 1
    print()


def get_number(lower, upper):
    should_try_again = True
    value = 0
    error_message = "Please enter an integer!"
    while should_try_again:
        try:
            value = int(input(f"Enter an integer({lower}, {upper}): "))
            if value < lower or value > upper:
                should_try_again = True
                print(error_message)
            else:
                should_try_again = False
        except ValueError:
            print(error_message)
    return value


if __name__ == "__main__":
    main()
