#Program to find the day of the month based on a given number day, number month, and number year

from sys import argv
from calendar import isleap, monthrange, weekday
from Input_Check import is_Number, is_Number_Range


#Displays an error message for an incorrect argument list
def error_Message_Argument_List():
	print("Error!! Wrong number of arguments. Sample on how to run this program:\n")
	print("py Calendar_Date.py 10 12 1995")
	
#Displays an error message for invalid members in the argument list
def error_Message_Invalid_Members():
	print("Error!! Invalid user input! Sample on how to run this program:\n")
	print("py Calendar_Date.py 10 12 1995")
	
#Finds and prints the day of the month for the given information from the command line arguments
#Each argument passed is a piece from the argument list passed as integers
#Uses the calendar weekday method and a list of the days as strings (day_List)
def day_Selection(day, month, year):
	day_List = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
	print(day_List[weekday(year, month, day)])
	
#---------------------------------------------------------------------------------------------	

#Check if the argument list contains the right number of arguments
if(len(argv) < 4 or len(argv) > 4):
	error_Message_Argument_List()
	
#Check if the year is a 4 digit number
if(len(argv[3]) != 4 or not is_Number(argv[3])):

	error_Message_Invalid_Members()
	
else:
	#Check if the Month is within the range of 12 months and is a number
	if(not is_Number_Range(argv[2], 1, 12)):
		error_Message_Invalid_Members()
		
	#Check if the days is a number
	elif(not is_Number(argv[1])):
		error_Message_Invalid_Members()
		
	else:
		storage = monthrange(int(argv[3]), int(argv[2]))
		
		#Check if the days are within the range for a given month and year
		if(int(argv[1]) > storage[1] or int(argv[1]) < 1):
			error_Message_Invalid_Members()
		else:
			day_Selection(int(argv[1]), int(argv[2]), int(argv[3]))