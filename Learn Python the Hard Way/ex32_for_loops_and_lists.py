for i in range(5):
    print("This is count %d" % (i+1))

fruits = ['apples', 'oranges', 'pears', 'apricots']
for fruit in fruits:
    print("A fruit of type: %s" % fruit)

change = [1, 'pennies', 2, 'dimes', 3, 'quarters']
for i in change:
    print("I got %r" % i)

elements = range(0, 6)
# for i in range(6):
# print("Adding %d to the list." % i)
# elements.append(i)

for i in elements:
    print("Element was: %d" % i)
