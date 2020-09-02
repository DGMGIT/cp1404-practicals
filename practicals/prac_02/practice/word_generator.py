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


def main():
    word_format = input("Enter the format: ").lower()
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


if __name__ == "__main__":
    main()
