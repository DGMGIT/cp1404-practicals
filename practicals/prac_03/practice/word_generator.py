"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
VOWEL = "v"
CONSONANT = "c"
WILDCARD = "*"
VOWEL_WILDCARD = "#"
CONSONANT_WILDCARD = "%"
TOKENS = [VOWEL, CONSONANT, WILDCARD, VOWEL_WILDCARD, CONSONANT_WILDCARD]


def main():
    should_try_again = True
    while should_try_again:
        word_format = input("Enter the format: ").lower()
        if not is_valid_format(word_format):
            print("Invalid format.\nTry again")
            should_try_again = True
        else:
            should_try_again = False

    word = ""
    for kind in word_format:
        if kind == WILDCARD:
            if random.randint(1, 2) == 1:
                word += random.choice(CONSONANTS)
            else:
                word += random.choice(VOWELS)
        elif kind == CONSONANT or kind == CONSONANT_WILDCARD:
            word += random.choice(CONSONANTS)
        elif kind == VOWEL or kind == VOWEL_WILDCARD:
            word += random.choice(VOWELS)
        else:
            word += kind
    print(word)


def is_valid_format(format):
    for letter in format:
        if letter not in TOKENS and not letter.isalpha():
            return False
    return True


if __name__ == "__main__":
    main()
