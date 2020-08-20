# Write code that asks the user for their name, then opens a file
# called "name.txt" and writes that name to it.
name = input("Enter your name: ")
outfile = open("name.txt", "w")
print(name, file=outfile)
outfile.close()

# Write code that opens "name.txt" and reads the name (as above) then
# prints, "Your name is Bob" (or whatever the name is in the file).
outfile = open("name.txt", "r")
read_name = outfile.readline()
print("Your name is {}".format(read_name))
outfile.close()

# Create a text file called numbers.txt and save it in your prac_02
# directory. Put the following three numbers on separate lines in
# the file and save it:
# 17
# 42
# 400
# Write code that opens "numbers.txt", reads only the first two
# numbers and adds them together then prints the result
numbers_file = open("numbers.txt", "w")
numbers = [17, 42, 400]
for number in numbers:
    print(number, file=numbers_file)
numbers_file.close()

numbers_file = open("numbers.txt", "r")
total = 0
for i in range(2):
    try:
        number = int(numbers_file.readline())
        total += number
    except ValueError:
        print("Non integer read")
numbers_file.close()
print("Result {}".format(total))

# Now write a fourth block of code that prints the total for all
# lines in numbers.txt or a file with any number of numbers.
numbers_file = open("numbers.txt", "r")
for line in numbers_file.readlines():
    print(line, end="")
numbers_file.close()
