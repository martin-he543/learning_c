from sys import argv


script, filename = argv  # use ex16_test.txt

print("We're going to erase %r." % filename)
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')  # setting 'w' truncates the file first, anyway.

print("Truncating the file. Goodbye!")
# target.truncate()  # Clears the file, though unnecessary

print("Now I'm going to ask you for three lines.")
line1 = str(input("line 1: "))
line2 = str(input("line 2: "))
line3 = str(input("line 3: "))

print("I'm going to write these to the file.")

# target.write(line1)  # Writes lines to the file
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")
target.write("%s\n%s\n%s" % (line1, line2, line3))

target.close()  # Closes and saves the file
