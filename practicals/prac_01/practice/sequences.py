start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

menu = "(E)ven numbers\n(O)dd numbers\n(S)quares\n(Q)uit"
print(menu)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "E":
        if start % 2 != 0:
            start += 1
        for i in range(start, end, 2):
            print(i, end=" ")
        print()
    elif choice == "O":
        if start % 2 == 0:
            start += 1
        for i in range(start, end, 2):
            print(i, end=" ")
        print()
    elif choice == "S":
        for i in range(start, end):
            print(i * i, end=" ")
        print()
    else:
        print("Invalid input")
    print(menu)
    choice = input(">>> ").upper()
print()
