#First Intermediate Program from reddit daily challenge
#Create a menu driven event organizer
#Will store event organizer in file called event_Organize.txt

from Day_Month_Check import date_Check
from Read_Write_File_1 import write_File
from Read_Write_File_1 import read_File

#User's choice
choice = 0

#Keeps track of the number of events in the system
eventCounter = 0

eventDetails = []
timeDetails = []
months = ["January", "February", "March", "April", "May", 
		"June", "July", "August", "September", "October", "November", "December"]

#Checks if string is an integer number
def is_number(s):
	try:
		int(s)
		return True
	except ValueError:
		return False
	
#Checks if a string is a number and sees if that number is within a range
#n1 is the lower part of the range and n2 is the higher part of the range	
def is_number_Range(s, n1, n2):
	try:
		int(s)
		
		if(int(s) < n1 or int(s) > n2):
			return False
			
		return True
	except ValueError:
		return False
	
#Displays the current events in the system
def displayEvents(eventCounter):
	if(eventCounter == 0):
		print("\nThere are no events to delete currently")
		return
		
	for num in range(0, eventCounter):
		print("\n", "#", num + 1, sep='')
		print("\n", timeDetails[num], sep='')
		print(eventDetails[num], sep='')
		
#Adds an event to the system		
def addEvent(eventCounter):
		
	month = input("\nEnter the month of the event(ex. March): ")
	while(not month in months):
		print("Please enter a valid month (ex. May)\n")
		month = input("Enter the month of the event: ")
		
	year = input("\nEnter the year of the event(ex. 2017): ")
	while(not is_number(year) or len(year) != 4):
		print("Please enter a valid year (ex. 2018)\n")
		year = input("Enter the year of the event: ")
		
	day = input("\nEnter the day of the event(ex. 15): ")
	while(not is_number(day) or not date_Check(int(day), month, int(year))):
		print("Please enter a valid day for your given Month(ex. 31 for January)\n")
		day = input("Enter the day of the event: ")
		
	hour = input("\nEnter in the hour of the event (1-12): ")
	if(not is_number_Range(hour, 1, 12)):
		print("Please enter a valid hour (ex. 6)")
		hour = input("\nEnter in the hour of the event (1-12): ")
		
	minute = input("\nEnter in the minutes of the event (00-59): ")
	if(not is_number_Range(minute, 0, 59) or len(minute) != 2):
		print("Please enter a valid minute (ex. 09)")
		minute = input("\nEnter in the minutes of the event (00-59): ")
		
	amPM = input("\nEnter if the event is AM or PM like shown: ")
	if(amPM != "AM" and amPM != "PM"):
		print("Please enter AM or PM")
		amPM = input("\nEnter if the event is AM or PM like shown: ")
	
	details = input("\nEnter a short description of your event: ")
	
	eventDetails.append(details)
	
	fullTime = hour + ":" + minute + amPM + " " + month + " " + day + ", " + year
	timeDetails.append(fullTime)
	
	eventCounter += 1
	return eventCounter
	
#Deletes an event from the system
def deleteEvent(eventCounter):
	if(eventCounter == 0):
		print("\nThere are no events to delete currently")
		return
		
	displayEvents(eventCounter)
	deletionChoice = input("Enter the number of the event you want to delete (ex. 1): ")
	if(not is_number(deletionChoice) or int(deletionChoice) < 0 or 
		int(deletionChoice) > eventCounter):
		print("Please enter a valid event choice from the list of events")
		deletionChoice = input("Enter the number of the event you want to delete (ex. 1): ")
	
	global eventDetails
	global timeDetails
	
	eventDetails.pop(int(deletionChoice) - 1)
	timeDetails.pop(int(deletionChoice) - 1)
	
	eventCounter -= 1
	return eventCounter
	
#Displays the main menu and gets the user's choice
def mainMenu():
	print("\nWelcome to the Event Organizer!\n")
	print("1. Add an Event")
	print("2. Delete an Event")
	print("3. View all events")
	print("4. Read a previous event file")
	print("5. Exit and write events to file")
	print("Choose option 4 if you have a previous file you would like to continue using")
	choice = input("\nChoose one of these options: ")
	return choice

#Decides what function to run based on the user's decision
def choiceSelection(currentChoice, eventCounter):
	if currentChoice == "1":
		eventCounter = addEvent(eventCounter)
		currentChoice = 0
		print(eventCounter)
		
	elif currentChoice == "2":
		eventCounter = deleteEvent(eventCounter)
		currentChoice = 0
		
	elif currentChoice == "3":
		displayEvents(eventCounter)
		currentChoice = 0
		
	elif currentChoice == "4":
		global eventDetails
		global timeDetails
		eventDetails, timeDetails, eventCounter = read_File(eventDetails, timeDetails)
		currentChoice = 0
		
	elif currentChoice == "5":
		currentChoice = "Exit"
		
	else:
		print("Please choose a valid option\n")

	return currentChoice, eventCounter
	
#Main loop of the program
while(choice == 0):
	choice = mainMenu();
	choice, eventCounter = choiceSelection(choice, eventCounter)

print("Thank you for using the event organizer! A file is being written currently for your events")

write_File(eventDetails, timeDetails, eventCounter)