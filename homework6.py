
import sys
'''
Beacuse sys.argv is a list sequence, we can pass arugments to learn more about it.
'''

#  Show the user the number of arguments passed with the len() function on the list, sys.argv.
print("Number of arguments:", len(sys.argv))

#  Display the arguments into strings with the str() function on the list, sys.argv. 
print("Argument list:", str(sys.argv))

print("Arguments made by user in reversed order: ", end = "" )

#  Sys.argv's first sequence, 0, is the file name, we will skip it.
#  Using brackets on a list, we can dictate the start and the end of a sequence.
#  Here we start the sequence at 1, showing us the arguments passed by the user input.
cheeses = sys.argv[1:]

#  Create a for loop.
#  Since we are working with a list, we can use the reversed() function to reverse the arguments made by the user.
#  We place the items of the sequence in reverse order into cheese.
for cheese in reversed(cheeses):

#  Create a new variable, out, to hold the information in cheese.
	out = "{}".format(cheese)

#  Output the arguments made by the user, stored inside the variable out.
	print(out, end = " ")

print()
