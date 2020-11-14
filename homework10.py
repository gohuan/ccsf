# Open file from linux servers
fhand = open("/users/abrick/resources/urantia.txt", "r")

# Store unique items in l
l = set()
for items in fhand:
	for thing in items.split(): 
		if thing not in l:
			l.add(thing)

# Count unique items from l
count = 0
for items in l:
	count = count + 1
print("The estimated number of unique words in the urantia text file:",count)

