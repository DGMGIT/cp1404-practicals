def main():
    password = get_password()
    print(hide_password(password))


def get_password():
    return input("Enter a password: ")


def hide_password(password):
    return "*" * len(password)


if __name__ == "__main__":
    main()
