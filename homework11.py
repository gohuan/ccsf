'''
CCSF CS131B
Author: Gordon Huang
Python Assignment 11
11/13/20
'''

import random
fhand = open('/users/abrick/resources/urantia.txt') # Open file


l = set()       # Create a sequence for items to populate
for items in fhand: 
    for a in items.split():      # Split lines into words, stored in a
        if a not in l: 
            l.add(a.strip('.,;'))      # Add unqiues to l while removing periods, commas, and semi-colons

l2 = set()      # Create a sequence for word lengths > than 10
for item in l:
    if len(item) > 10:
        l2.add(item)

def rand():     # Make function to remove dupes
    l3 = set()
    for n in range(0,10): 
        a = random.choice(tuple(l2))
        if a not in l3:
            l3.add(a)
    return l3   # Return set, l3, with 10 random words from the urantia text file


print("10 unqiue words with lengths greater than 10:", rand())


fhand.close()   # Close file
