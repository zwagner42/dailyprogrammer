# Password Protected Program.  Waits until proper password is entered before running program.
# Uses the file loginInformation.txt to store usernames and passwords
# This program is not very secure since anyone can just enter in new information to get into
# The system but it does prevent people who don't from entering with knowing information already
# Also easily breakable if you now how to 

from Generic_File import generic_Read, generic_Write
from Input_Check import is_Number_Range
import hashlib

#Function for checking if the user name is duplicate to an existing user name
#userName is the entered user name from the user
#numUserNames is the number of already existing user names
#informationList is the list of user name and password information
def check_UserName(userName, numUserNames, informationList):
	
	for num in range(0, numUserNames):
		userStorage = informationList[num].split()
		if(str((hashlib.md5(userName.encode("utf-8"))).hexdigest()) == userStorage[0]):
			return False
	
	return True

#Function for checking if the login information is valid
#userInformation is the entered user information from the user
#numUserInformation is the number of login credentials already in existence 
#informationList is the list of user name and password information
def check_Login(userInformation, numUserInformation, informationList):
	
	
	for num in range(0, numUserInformation):
		userStorage = informationList[num].split()
		if(str((hashlib.md5(userInformation[0].encode("utf-8"))).hexdigest()) == userStorage[0]):
			if(str((hashlib.md5(userInformation[1].encode("utf-8"))).hexdigest()) == userStorage[1]):
				return True
	
	return False
	
#Function for enter login information
def login_Information():
	#Message to user and get their input
	print("\nLogin Information (If you would like out of this section type in # into the user name)")
	userName = input("\nEnter your user name: ")
	
	#Check for exit condition
	if(userName == "#"):
		return
		
	password = input("\nEnter your password: ")
		
	#Add user information into a list
	userInfo = []
	userInfo.extend([userName, password])
	
	#Get login information
	informationList = generic_Read("loginInformation.txt")
	
	#Loop until proper login information is entered or exit condition is entered
	while(not check_Login(userInfo, len(informationList), informationList)):
		print("\nInvalid login information!\n")
		print("\n(Remember,  you can exit this portion by entering # as your user name)")
		userName = input("\nEnter your user name: ")
		
		if(userName == "#"):
			return
			
		password = input("\nEnter your password: ")
		
		userInfo = []
		userInfo.extend([userName, password])
		
	#Print reward for getting here
	print("\nYOU GOT HERE !!!!!!!!!\n. . . That's it\n")
		
#Function for entering in login information
def enter_Information():
	#List for writing to a file
	writeList = []

	#Get user name
	userName = input("\nEnter in an user name (Do not choose # as your user name): ")
	informationList = generic_Read("loginInformation.txt")
	
	#Check user name so that it there is not a duplicate already
	while(not check_UserName(userName, len(informationList), informationList) or userName == "#"):
		print("\nAlready Exist\n")
		userName = input("\nEnter in an user name: ")
	
	userName = hashlib.md5(userName.encode("utf-8")).hexdigest()
		
	#Get Password
	password = hashlib.md5((input("\nEnter in a password: ")).encode("utf-8")).hexdigest()
	
	writeStorage = str(userName) + " " + str(password)
	
	writeList.append(writeStorage)
	generic_Write("loginInformation.txt", writeList)
	
#Function to display the main menu and get the user input for the main menu
def main_Menu():
	print("\nWelcome to a simple login program!")
	print("\n1. Enter new login information (Choose if you have no login information)")
	print("\n2. Login in with existing information")
	print("\n3. Exit Program")

	user_Choice = input("\nEnter your choice (1 through 3): ")

	while (not is_Number_Range(user_Choice, 1, 3)):
		print("\nInvalid choice!  Please enter in a valid choice.\n")
		return 0

	if user_Choice == "1":
		enter_Information()
		return 0
	elif user_Choice == "2":
		login_Information()
		return 0
		
	else:
		return 3


choice = 0
while (choice != 3):
	choice += main_Menu();
	
print("\nThank you for using the program!")
