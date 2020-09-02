# Question 1
# Write a program that prompts the user for 5 numbers and then stores each of
# these in a list called numbers. The program should then output various
# interesting things, as in the output below. Note that you can use the
# functions min, max, sum and len, and you can use the append method to add
# a number to a list.

MAX_INPUT_COUNT = 5


def main():
    # Question 1
    numbers = []
    for number in range(1, MAX_INPUT_COUNT + 1):
        value = get_int(f"Number {number}: ")
        numbers.append(value)
    print_list_infomation(numbers)
    # Question 2
    # Ask the user for their username. If the username is in the above list of
    # authorised users, print "Access granted", otherwise print "Access denied"
    usernames = [
        'jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
        'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
        'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob'
    ]
    username = input("Enter your username: ")
    if username in usernames:
        print("Access granted")
    else:
        print("Access denined")


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


def print_list_infomation(my_list):
    print(f"The first number is {my_list[0]}")
    print(f"The last number is {my_list[-1]}")
    print(f"The smallest number is {min(my_list)}")
    print(f"The largest number is {max(my_list)}")
    average = sum(my_list) / len(my_list)
    print(f"The average of the numbers is {average}")


if __name__ == "__main__":
    main()
