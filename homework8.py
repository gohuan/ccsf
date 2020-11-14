import sys

# Containers 2 hw
stored_arg = sys.argv[1:]
arg_dict = dict() # Followed the example from Severance 9 where he created a for loop to place items into a dictionary.

for item in stored_arg:
	arg_dict[item] = arg_dict.get(item, 0) + 1

arg_sorted = sorted(arg_dict) # Followed the instructor's notes to sort key alphabetically.

# Amend homework to make arguments uppercase
save = []
mark = set()
for i in arg_sorted:
	l = i.lower()
	if l not in mark:
		mark.add(l)
		save.append(i.upper())
save = sorted(save)
print(save)
