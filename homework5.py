'''
CS131B Assignment
Simulate a throw of two 900-sided dice and indicates 
whether or not the sum of the results is divisible by three.
'''

import random

# Model the roll of two 900 sided die
die_roll1 = random.randint(1,900)
die_roll2 = random.randint(1,900)

''' Use branching to determine whether the sum of the results is divisible by 3.'''

# Sum of the two rolls
rollsum = die_roll1 + die_roll2


# Use conditionals to determine if the sum is divisible by 3.
if rollsum%3 == 0:
    output = "Amazingly, the simulated roll of your dice, {:}, was divisible by 3!".format(rollsum)
    print(output)
else:
    output = "The simulated roll of your dice, {:}, was unfortunately not divisible by 3.".format(rollsum)
    print(output)
