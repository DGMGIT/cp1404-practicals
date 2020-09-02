import random


MAX_PICKS = 6
MIN_VALUE = 1
MAX_VALUE = 45


def main():
    picks_amount = get_int("How many quick picks? ")
    for pick in range(picks_amount):
        picks = generate_picks(MAX_PICKS, MIN_VALUE, MAX_VALUE)
        picks.sort()
        print(format_picks(picks))


def get_int(prompt):
    should_try_again = True
    value = 0
    while should_try_again:
        try:
            value = int(input(prompt))
            should_try_again = False
        except ValueError as e:
            print("Enter an integer: ")
            should_try_again = True
    return value


def generate_picks(amount, min_pick, max_pick):
    picks = []
    for i in range(amount):
        random_value = random.randint(min_pick, max_pick)
        picks.append(random_value)
    return picks


def format_picks(picks):
    string = ""
    for value in picks:
        string += "{:>2} ".format(value)
    return string


if __name__ == "__main__":
    main()
