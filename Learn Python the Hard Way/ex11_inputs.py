print("How old are you?"),
age = input()  # has security flaws... ?
print("How tall are you?"),
height = input()
print("How much do you weigh?"),
weight = input()

print("So you're %r years old, %r tall and %r heavy." % (age, height, weight))
