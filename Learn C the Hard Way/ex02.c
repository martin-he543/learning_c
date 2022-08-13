/* Exercise 2 was the following makefile:

CFLAGS=-Wall -g

# "all" target runs with just the command, "make"
all:
	make ex01
	./ex01
	make ex03
	./ex03

# This is known as a target.
clean:
	rm -f ex01
	rm -f ex03
# Must be intented to prevent "missing separator error".


*/