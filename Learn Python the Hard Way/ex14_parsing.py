from sys import argv

script, user_name = argv
# prompt = '> ' Not using raw_input(prompt) function because it is deprecated in python3

print("Hi %s, I'm the %s script." % (user_name, script))
print("I'd like to ask you a few more questions.")

likes = input("Do you like me %s?" % user_name)
lives = input("Where do you live, %s?" % user_name)
computer = input("What kind of computer do you have, %s?" % user_name)

print("""
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer))
