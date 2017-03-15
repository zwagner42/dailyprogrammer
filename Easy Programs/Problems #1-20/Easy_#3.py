#Simple alphabetical caesar cipher.  Uses a randomly generated key between 1 and 26

from random import randint

def check_String(textList):
	for char in textList:
		if(char != ' ' and not char.isalpha()):
			return False
			
	return True
	
def encode_String(text):
	key = randint(1, 26)
	asciiList = []
	asciiStorage = 0
	
	for index in range(0, len(text)):
		if(text[index] != " "):
			asciiStorage = ord(text[index]) + key
			if(ord(text[index]) >= 97):
				
				if(asciiStorage > 122):
					asciiStorage = asciiStorage % 122 + 97
				
				asciiList.append(asciiStorage)
			else:
				
				if(asciiStorage > 91):
					asciiStorage = asciiStorage % 91 + 65 
				
				asciiList.append(asciiStorage)
		else:
			asciiList.append(32)
			
	print(asciiList)
	
	return ''.join(chr(i) for i in asciiList), key

def decode_String(encoded_Text, key):
	asciiList = []
	asciiStorage = 0
	
	for index in range(0, len(encoded_Text)):
		if(encoded_Text[index] != " "):
			asciiStorage = ord(encoded_Text[index]) - key
			if(ord(encoded_Text[index]) >= 97):
				
				if(asciiStorage > 122):
					asciiStorage = asciiStorage % 122 + 97
				elif(asciiStorage < 97):
					asciiStorage = asciiStorage + 25
				
				asciiList.append(asciiStorage)
			else:
				
				if(asciiStorage > 91):
					asciiStorage = asciiStorage % 91 + 65 
				elif(asciiStorage < 65):
					asciiStorage = asciiStorage + 26
				
				asciiList.append(asciiStorage)
		else:
			asciiList.append(32)
			
	print(asciiList)
	
	return ''.join(chr(i) for i in asciiList), key
	
text = input("Enter the text you would like encrypted (Please only include alphabetical letters): ")

print(text)

while(not check_String(list(text))):
	print("\nInvalid input!  Example of valid input -A long walk on the street-")
	text = input("\nEnter the text you would like encrypted (Please only include alphabetical letters): ")
	
encoded_Text, key = encode_String(text)
decoded_Text, key = decode_String(encoded_Text, key)

print("Encrypted Text: ")
print(encoded_Text)
print("Decrypted Text: ")
print(decoded_Text)
	
print("\nEnd")