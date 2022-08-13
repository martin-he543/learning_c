# Solve the quadratic equation ax**2 + bx + c = 0

# import complex math module
import cmath
import math

print("Let's solve quadratic equation!")

print('Please enter value of a, b, c')
a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

#sol3 = (-b-math.sqrt(d))/(2*a)
#sol4 = (-b+math.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1, sol2))
#rint('The solution are {0} and {1}'.format(sol3, sol4))
