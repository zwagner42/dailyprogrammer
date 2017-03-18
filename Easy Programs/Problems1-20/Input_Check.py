#File for various input checks I have come up with over time.
#Might not include everything

#Checks if a string is a number and sees if that number is within a range
#n1 is the lower part of the range and n2 is the higher part of the range	
def is_Number_Range(s, n1, n2):
	try:
		int(s)
		
		if(int(s) < n1 or int(s) > n2):
			return False
			
		return True
	except ValueError:
		return False