"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random


def main():
    score = float(input("Enter score: "))
    result = get_result(score)
    print(result)
    random_score = random.randint(0, 100)
    print("score: {} result: {}".format(random_score,
          get_result(random_score)))


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
