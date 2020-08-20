for i in range(1, 21, 2):
    print(i, end=" ")
print()

for i in range(0, 110, 10):
    print(i, end=" ")
print()

for i in range(20, 0, -1):
    print(i, end=" ")
print()

num_of_stars = int(input("Number of stars: "))
# print(f"{'*' * num_of_stars}")
for i in range(0, num_of_stars):
    print("*", end="")
print()
for i in range(0, num_of_stars):
    for j in range(0, i + 1):
        print("*", end="")
    print()
# print()
