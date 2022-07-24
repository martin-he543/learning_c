import numpy as np
a, b, c = input("Enter coefficients of ")

discriminant = np.sqrt(b**2 - 4*a*c)
sol_1, sol_2 = (-b + discriminant)/(2*a), (-b - discriminant)/(2*a)
