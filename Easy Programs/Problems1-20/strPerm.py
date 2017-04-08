#! python3
# strPerm - Takes a string in from the command line and returns all permutations of that string

import sys, itertools

#If the program is run with invalid arguments
if len(sys.argv) != 2:
	print("Error: No String Given")
	print("\n Usage: py strPerm.py <string>")
	print("\n Ex. py strPerm.py hello")
	
else:
	#Create a list to contain all the permutations
	permList = []
	#Loop through the contents from the itertools.permutations method
	#This works since itertool.permutations returns an iterator for the permutations of the
	#Passed Iterable
	for x in itertools.permutations(sys.argv[1]):
		permList.append(''.join(x))
	print(permList)