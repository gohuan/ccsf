import sys

stored_arg = sys.argv[1:]
arg_dict = dict() # Followed the example from Severance 9 where he created a for loop to place items into a dictionary.

for item in stored_arg:
	arg_dict[item] = arg_dict.get(item, 0) + 1

arg_sorted = sorted(arg_dict) # Followed the instructor's notes to sort key alphabetically.
print(' '.join(arg_sorted))

