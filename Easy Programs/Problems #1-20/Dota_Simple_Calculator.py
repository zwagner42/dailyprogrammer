#Easy_#2 program where we will make a calculator for magic damage calculations in Dota 2
#Physical damage calculations are much more difficult and require their own seperate program

choice = 0
magicResist = 0
damage = 0 
totalDamage = 0
		
def mainMenu():
	print("Welcome to the Dota 2 Damage Calculator!\n")
	print("1. Magic Damage")
	print("2. Exit Calculator")
	choice = input("Which option do you choose: ")
	return choice

def is_number(s):
	try:
		float(s)
		return True
	except ValueError:
		return False
	
def choiceOne():
	damage = input("\nWhat is the amount of magic damage being dealt: ")
	while(not is_number(damage) or float(damage) < 0):
		print("Please input a proper damage number (a positive number)")
		damage = input("\nWhat is the amount of magic damage being dealt: ")
	magicResist =  input("What is the percentage amount of  magic resistance the target has (ex. 0.34 for 34%): ")
	while(not is_number(magicResist) or float(magicResist) < 0 or float(magicResist) >= 1):
		print("Please input a proper magic resistance value (ex. 0.23 is 23%)")
		magicResist =  input("\nWhat is the percentage amount of  magic resistance the target has (ex. 0.34 for 34%): ")
	totalDamage = float(damage) - (float(damage) * float(magicResist))
	print("\nThe total damage taken is ", totalDamage, sep='')
	return

	
def choiceSelection(choice):
	if choice == '1':
		choiceOne()
		choice = 0
		
	elif choice == '2':
		choice == "Exit"
		
	else:
		print("Please select a valid option!\n")
	return choice

while(choice == 0):
	choice = mainMenu()
	choice = choiceSelection(choice)

print("Thank you for using this calculator!")
