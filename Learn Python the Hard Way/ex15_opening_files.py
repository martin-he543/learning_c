from sys import argv

script, filename = argv
txt = open(filename)  # Opens Python File returning String

print("Here's your file %r:" % filename)
print(txt.read())  # Reads the Python File
txt.close()  # Remember to close file after opening

file_again = input("Type the filename again: \n> ")
txt_again = open(file_again)
print(txt_again.read())
txt_again.close()
