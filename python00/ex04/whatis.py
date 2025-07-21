import sys as sys

nb_count = len(sys.argv)

if nb_count == 1:
	sys.exit()

if nb_count > 2:
	print("AssertionError: more than one argument is provided")
	sys.exit()

try:
	nb = int(sys.argv[1])
	if nb % 2 == 0:
		print("I'm Even.")
	else:
		print("I'm Odd.")
except ValueError:
	print("AssertionError: argument is not an integer")
