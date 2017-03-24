#Validates that a phone number entered is valid.
#First program to test using regular expressions
#Thus, all of the following are valid telephone numbers:
#1234567890, 123-456-7890, 123.456.7890, (123)456-7890,
#(123) 456-7890 
#(note the white space following the area code),
# and 456-7890.


#import for regex
import re

phone_Number = ''

reg_Ex = '\\([0-9]{3}\\)[0-9]{3}[-.]?[0-9]{4}$|([0-9]{3}[-.]?){2}[0-9]{4}$|[0-9]{3}[-.]?[0-9]{4}$'

#Loop for inputting telephone numbers 
while(phone_Number != '!!!'):
	phone_Number = input("Please enter a phone number: ")

	#Get rid of white space
	phone_Number = ''.join(phone_Number.split())
	
	reg1 = re.match(reg_Ex, phone_Number, flags=0)

	if reg1:
		print(reg1.group(0))
	else:
		print("Invalid Input!!")