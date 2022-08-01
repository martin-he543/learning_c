formatter = "%r %r %r %r"

print(formatter % (1, 2, 3, 4))
# outputs with single quotes
print(formatter % ("one", "two", "three", "four"))
print(formatter % (True, False, True, False))
print(formatter % (formatter, formatter, formatter, formatter))

print(formatter % ("I had this one thing", "That you could type up right.",
      "But it didn't sing.", "So I said goodnight."))
# Note the third line outputs the single quotes.
