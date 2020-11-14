import sys

stored_args = sys.argv[1:]
arg_dict = dict()

for item in stored_args:
    if item not in arg_dict:
        arg_dict[item] = 1
    else:
        arg_dict[item] = arg_dict[item] + 1
arg_sorted = sorted(arg_dict)
print(' '.join(arg_sorted))
