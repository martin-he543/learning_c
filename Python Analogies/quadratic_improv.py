import numpy as np
import matplotlib.pyplot as plt
a, b, c = float(input("Enter coefficients of a quadratic expression:\n a = ")), float(
    input(" b = ")), float(input(" c = "))
discriminant = b**2 - 4*a*c

# Distinct roots
if discriminant > 0:
    sol_1, sol_2 = (-b + np.sqrt(discriminant)) / \
        (2*a), (-b - np.sqrt(discriminant))/(2*a)
    print("There are two real solutions:\nx = ", sol_1, ',', sol_2)

    x = np.linspace(sol_1 - (sol_2 - sol_1)/2, sol_2 + (sol_2 - sol_1)/2, 1000)
    plt.plot(x, a*x**2+b*x+c)
    plt.plot(x, np.zeros(len(x)), '--')
    plt.plot(sol_1, 0, 'o')
    plt.plot(sol_2, 0, 'o')
    plt.grid()
    plt.show()

# Repeated roots
elif discriminant == 0:
    sol_1 = (-b + np.sqrt(discriminant))/(2*a)
    print("There is one real solution:\nx = ", sol_1)

    x = np.linspace(sol_1 - 1/2, sol_1 + 1/2, 1000)
    plt.plot(x, a*x**2+b*x+c)
    plt.plot(x, np.zeros(len(x)), '--')
    plt.plot(sol_1, 0, 'o')
    plt.grid()
    plt.show()

# Complex conjugate roots
else:
    sol_1, sol_2 = (-b + np.lib.scimath.sqrt(discriminant)) / \
        (2*a), (-b - np.lib.scimath.sqrt(discriminant))/(2*a)
    print("There are no real solutions.\nx = ", sol_1, ',', sol_2)
