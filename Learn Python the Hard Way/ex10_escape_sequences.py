from os import wait


tabby_cat = "\tI'm tabbed in."  # types a tab
persian_cat = "I'm split\non a line."  # types on new line
backslash_cat = "I'm \\ a \\ cat"  # types backslash

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
# creates a tabbed to-do list, including "Grass"

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

print("\u232c\u5350\u97d3hello")  # successive "interesting" characters

while True:
    for i in ["/", "-", "\\", "|"]:  # clever use of a for loop
        # carriage return and print one of the above strings.
        print("%s\r" % i)

# List of All Escape Sequences

# \\      Backslash
# \'      Single Quote
# \"      Double Quote
# \a      ASCII bell(BEL)
# \b      ASCII backspace(BS)
# \f      ASCII formfeed(FF)
# \l      ASCII linefeed(LF)
# \r      ASCII carriage return (CR)
# \t      ASCII horizontal tab(TAB)
# \v      ASCII vertical tab

# \ooo    Character with octal value oo
# \xhh    Character with hex value hh

# \N{name}    Character named in Unicode database(Unicode only)
# \uxxxx      Character with 16-bit hex value(Unicode only)
# \uxxxxxxxx  Character with 32-bit hex value(Unicode only)
