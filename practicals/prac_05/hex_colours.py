HEX_COLOURS = {
    "red1": "#ff0000", "magenta": "#ff00ff", "yellow1": "#ffff00",
    "white": "#ffffff", "violet": "#ee82ee", "green1": "#00ff00",
    "hotpink": "#ff69b4", "gray": "#bebebe", "black": "#000000",
    "coral": "#ff7f50",
}


def main():
    colour = get_string("Enter a colour: ")
    while len(colour) != 0:
        print("{} -> {}".format(colour, HEX_COLOURS[colour]))
        colour = get_string("Enter a colour: ")
    print("program end")


def get_string(prompt):
    return input(prompt).strip().lower()


if __name__ == "__main__":
    main()
