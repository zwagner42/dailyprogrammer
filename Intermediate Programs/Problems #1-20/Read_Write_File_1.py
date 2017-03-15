#Python Script for writing a to a file specific to Problem#1 of the Intermediate reddit problems
		

#Writes information from the system in Intermediate_#1.py into a file 
#eventDetailsList is the list from Intermediate_#1.py that stored the event details
#timeDetailsList is the list from Intermediate_#1.py that stored the time information for an event
#eventCounter is the number of events in the system from Intermediate_#1.py when the write operation is called
#The information is written to a file called EventOrganization.txt
def write_File(eventDetailsList, timeDetailsList, eventCounter):

	target = open("EventOrganization.txt", "w")
	
	for num in range(0, eventCounter):
		target.write(timeDetailsList[num] + "\n")
		target.write(eventDetailsList[num] + "\n")
		target.write("-----\n")
	target.close()
	
#Read the EventOrganization.txt and store its information in the system of Intermediate_#1.py
#eventDetailsList is the list from Intermediate_#1.py that stored the event details
#timeDetailsList is the list from Intermediate_#1.py that stored the time information for an event
def read_File(eventDetailsList, timeDetailsList):
	try:
		target = open("EventOrganization.txt", "r")
		counter = 0
		
		for line in target:
			if(line != "-----\n"):
				line = line[:-1]
				timeDetailsList.append(line)
				line = target.readline()
				line = line[:-1]
				eventDetailsList.append(line)
				counter += 1
		
		return eventDetailsList, timeDetailsList, counter
			
	except IOError:
		print("A previous event organization file does not exist!")