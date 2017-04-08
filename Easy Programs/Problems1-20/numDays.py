#! python3
# numDays.py - Finds the number of days that have pasted in a year given a month and day
# Month is entered by its name (Ex. Janurary)  and the day is entered as a number (Ex. 1)
# Program assumes no leap years and adds in the end date

from sys import exit, argv

#Function to print the usage message
def usage_Message():
	print("Usage:  py numDays.py <month> <day>")
	print("\nEx. py numDays.py January 12")

#If incorrect arguments are given
if len(argv) != 3:
	print("Error running this program!\n")
	usage_Message()
	exit()
	
else:
	#Dictionary holding the day information for each month
	day_Nums = {"JANUARY": [0, 31], "FEBRUARY": [31, 59], "MARCH": [59, 90], "APRIL": [90, 120],
				"MAY": [120, 151], "JUNE": [151, 181], "JULY": [181, 212], "AUGUST": [212, 243],
				"SEPTEMBER": [243, 273], "OCTOBER": [273, 304], "NOVEMBER": [304, 334],
				"DECEMBER": [334, 365]}
	
	#Try and Except block to act as error checking for the arguments given
	try:
		#Get the day information from the user's given month
		month_Info = day_Nums[argv[1].upper()]
		
		#Check that the day given is in the month given
		if(int(argv[2]) <= 0 or int(argv[2]) + month_Info[0] > month_Info[1]):
			raise Exception()
		else:
			#Get and print the number of days that have past
			pastDays = int(argv[2]) + month_Info[0]
			print("The number of days that have past this is year is " + str(pastDays))
			print("Note:  This date has the end date added to it")
	except (KeyError, ValueError, Exception):
		print("Error with Month or Day entered!\n")
		usage_Message()