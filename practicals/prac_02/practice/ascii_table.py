LOWER = 33
UPPER = 127


def main():
    char = input("Enter a character: ")
    print("The ASCII code for {} is {}".format(char, ord(char)))

    try_again = True
    while try_again:
        try:
            ascii_code = int(input("Enter a number between 33 and 127: "))
            if ascii_code < LOWER or ascii_code > UPPER:
                try_again = True
            else:
                try_again = False
        except ValueError:
            print("Please enter an interger.")
            try_again = True
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


main()
