
import sys
'''
cheeses = sys.argv()
for cheese in reversed(cheeses):
	out = "{}".format(cheese)
	print(out, end = ' ')
print()
'''
print(' '.join(reversed(sys.argv[1:])))
