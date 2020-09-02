import sys
import random


FILE_NAME = "temps_input.txt"


def main():
    if len(sys.argv) != 4:
        print("Usage\npython3 create_temps.py number_of_temps min_temp" +
              " max_temp")
        sys.exit()

    try:
        number_of_temps = int(sys.argv[1])
        min_temp = int(sys.argv[2])
        max_temp = int(sys.argv[3])
    except ValueError as e:
        print(e)
        sys.exit()

    if number_of_temps <= 0:
        print("number of temperatures musts be greater than 0")
        sys.exit()

    if min_temp >= max_temp:
        print("min temp ({}) must be less than max temp ({})".format(min_temp,
              max_temp))
        sys.exit()

    temps_file = open(FILE_NAME, 'w')
    for i in range(number_of_temps):
        rand_temp = random.randint(min_temp, max_temp)
        print(rand_temp, file=temps_file)
    temps_file.close()


if __name__ == "__main__":
    main()
