#Function for checking proper range of dates in a month

#day is the number day of the month as an integer
#month is the month of the given day as a string
#year is the year of the given day and month as a integer
#Returns False if any invalid conditions are met
#Returns True if all conditions for the day and month are valid

def date_Check(day, month, year):
	thirtyOneMonths = ["January", "March", "May", "July", "August", "October", "December"]
	thirtyMonths = ["April", "June", "September", "November"]
	
	if(day < 0 or day > 31):
		return False
	elif(month == "February"):
		if(day > 29):
			return False
		elif(year % 4 != 0 and day == 29):
			return False
		else:
			return True
	elif(month in thirtyMonths):
		if(day == 31):
			return False
		else:
			return True
	return True