'''
CS131B: Determine what portion of the global population has 
permanent representation on the United Nations Security Council.

According to the United Nations Security Council, there are 5 permanent
members of the council which includes China, France, Russia, UK, and the US. 

To find what portion of the global population has permanent representation,
I will find the population of the countries permanently represented members divided by the total global population.

Population of the permanent members in 2020.
China: 1,439,323,776 according to Worldometer (https://www.worldometers.info/world-population/china-population/)
France: 65,273,511 accoridng to Worldometer (https://www.worldometers.info/world-population/france-population/)
Russia: 145,934,462 according to Worldometer (https://www.worldometers.info/world-population/russia-population/)
UK: 67,866,011 according to Worldometer (https://www.worldometers.info/world-population/uk-population/)
US: 331,002,651 according to Worldometer (https://www.worldometers.info/world-population/us-population/)
Sum of the permanent member population: 2,049,400,411

Global population in 2020.
7,794,798,739 (https://www.worldometers.info/world-population/#:~:text=The%20current%20world%20population%20is,currently%20living)%20of%20the%20world.)

Population represented by the permanent members of the United Nations Security Council:
Population of permanent members / global population 
'''

# Determine the population of the UNSC permanently represented members
china_pop = 1439323776
france_pop = 65273511
russia_pop = 145934462
uk_pop = 67866011
us_pop = 331002651
permanent_memb_pop = china_pop + france_pop + russia_pop + uk_pop + us_pop

# Determine the population of the world
global_pop = 7794798739

# Determine the portion of the population permanently represented by the UNSC by dividing 
# the population permanently represented by the UNSC over the global population
portion_perm_rep = (float(permanent_memb_pop / global_pop))

# Output
output = "{:%} or {:} of the world population is permanently represented by the United Nations Security Council.".format(portion_perm_rep, portion_perm_rep)

# Print
print(output)






