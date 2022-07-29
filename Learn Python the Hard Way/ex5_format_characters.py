my_name = 'Martin A. He'
my_age = 19
my_height = 175
my_weight = 63.6
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Black'

print("Let's talk about %s" % my_name)
print("He's %d cm tall." % my_height)
print("He's %d kg heavy." % my_weight)
print("Actually that's not that heavy.")
print("He's got %s eyes and %s hair" % (my_eyes, my_hair))
print("His teeth are usually %s depending on the coffee." % my_teeth)

print("If I add %d, %d, and %d, I get %d." %
      (my_age, my_height, my_weight, my_age+my_height+my_weight))

# The %r Python formatter.
print("This is me trying different variables with: %r, %r, and %r" %
      (my_name, my_age, my_weight))

# How to round integers.
print(round(my_weight))
print("This is the answer in octal: %o" % my_age)

"""
List of Python Format Characters
%d - integers
%f - floating points
%b - binary
%o - octal
%x - octal hexadecimal
%s - string
%e - floating point exponents
"""
