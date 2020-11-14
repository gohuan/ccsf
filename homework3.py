''' Each state has two senators no matter the population.
We must determine how much more Senate representation Idaho residents have compared to Florida.
Idaho Population: 1,787,065 
According to Wiki, Source: "Population, Population Change, and Estimated Components of Population Change: April 1, 2010 to July 1, 2019 (NST-EST2019-alldata)". Census.gov. United States Census Bureau. Archived from the original on January 26, 2020. Retrieved February 8, 2020.
Florida Population: 21,477,737 
According to Wiki, Source: Population, Population Change, and Estimated Components of Population Change: April 1, 2010 to July 1, 2019 (NST-EST2019-alldata)". Census.gov. United States Census Bureau. Archived from the original on January 26, 2020. Retrieved February 8, 2020.
'''
florida = 21477737
idaho = 1787065
representation = florida / idaho

print("Population of Idaho:", idaho)
print("Population of Florida:", florida)
print("Idaho residents have", round(representation,2), "more senate representation power compared to Florida residents.")

