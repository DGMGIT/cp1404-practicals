"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    try_again = True
    while try_again:
        if denominator == 0:
            try_again = True
            denominator = int(input("Enter the denominator: "))
        else:
            try_again = False
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# When will a ValueError occur?
# when the input to numerator or denominator fail to cast
# When will a ZeroDivisionError occur?
# when denominator is 0
# Could you change the code to avoid the possibility of a ZeroDivisionError?
# ask for input again until the number isn't 0