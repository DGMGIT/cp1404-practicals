def main():
    name_to_email = {}

    email = input("Enter your email: ").strip()
    while len(email) != 0:
        name = get_name_from(email)
        answer = get_response("Is your name {}? y/n ".format(name))
        if answer == 'y':
            if name in name_to_email and name_to_email[name] == email:
                print("That name and email already exists")
            else:
                name_to_email[name] = email
        else:
            name = input("Name: ")
            name_to_email[name] = email
        email = input("Enter your email: ").strip().lower()

    for key in name_to_email:
        print("{} ({})".format(key, name_to_email[key]))


def get_name_from(email):
    first_chunk = email.split("@")
    if len(first_chunk) == 0:
        print("Invalid email")
        return
    names = first_chunk[0].split(".")
    names = [name.title() for name in names]
    name = " ".join(names)
    return name


def get_response(prompt):
    should_try_again = True
    answer = ""
    while should_try_again:
        should_try_again = False
        answer = input(prompt).strip().lower()[0]
        if len(answer) == 0 or answer == 'y':
            answer = 'y'
        elif answer == 'n':
            answer = 'n'
        else:
            print("Invalid answer. Try again: ")
            should_try_again = True
    return answer


if __name__ == "__main__":
    main()
