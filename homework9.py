import sys
s = sys.argv[1:]

# Raise an exception if the argument list contains a non-numeric
for item in s:
	if item.isalpha() == False:
		raise TypeError ("Non-numerics are not accepted in the argument list.")

len_stored = 0
for item in s:
	a = int(len(item))
	len_stored = a + len_stored
print(len_stored)
