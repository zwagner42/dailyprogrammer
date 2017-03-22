#Sorts the input the user gives. Numerically for numbers and Alphabetically for letters.

sort_List = []

for char in input("Enter what you would like sorted: "):
	sort_List.append(char)
	
sort_List.sort()
print(sort_List)