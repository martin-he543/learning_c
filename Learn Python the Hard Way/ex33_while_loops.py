i, numbers = 0, []


def tester(i):
    if i >= 6:
        return False


# while i < 6:
while True:
    print("At the top i is %d" % i)
    numbers.append(i)
    i += 1
    print("Numbers now:", numbers)
    print("At the bottom i is %d" % i)

    if tester(i) == False:
        break

print("The numbers: ")
for num in numbers:
    print(num)
