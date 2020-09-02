import random


MIN_SCORE = 0
MAX_SCORE = 100
FILE_NAME = "results.txt"


def main():
    should_try_again = True
    while should_try_again:
        try:
            number_of_scores = int(input("Enter a number of scores: "))
            should_try_again = False
        except ValueError:
            print("Error. Enter an integer")
            should_try_again = True

    output_file = open(FILE_NAME, "w")
    for i in range(number_of_scores):
        random_score = random.randint(MIN_SCORE, MAX_SCORE)
        result = get_result(random_score)
        print("{} is {}".format(random_score, result), file=output_file)
    output_file.close()


def get_result(score):
    result = ""
    if score < 0 or score > 100:
        result = "Invalid score"
    else:
        if score >= 90:
            result = "Excellent"
        elif score >= 50:
            result = "Passable"
        else:
            result = "Bad"
    return result


if __name__ == "__main__":
    main()
