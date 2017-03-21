#Generic function for reading a file.  Reads each line in into a list as strings.

#Reads from a file and returns a list containing each read line
#fileName is the file to be read from
def generic_Read(fileName):
	try:
		target = open(fileName, "r")
		lineList = []
		for line in target:
			if(line.endswith("\n")):
				lineList.append(line[:-1])
			else:
				lineList.append(line)
			
		target.close()
		return lineList
	except IOError:
		print("\nInvalid file name!")

#Writes to a given file.  Appends the information to the file.
#fileName is the file to be written to
#writeList is the list of information to write to the file	
def generic_Write(fileName, writeList):
	try:
		target = open(fileName, "a")
		
		for line in writeList:
			target.write(line)
			
		target.close()
	except:
		print("\nError writing to the file!")