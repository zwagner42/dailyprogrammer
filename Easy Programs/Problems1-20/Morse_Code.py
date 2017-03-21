#A Morse Code Translator.  Reads Morse code from a file (morse_code.txt) as formatted in the file.

from Generic_File import generic_Read, generic_Write

#Dictionary containing the mapping to each letter and number in morse code
morse_mapping_string = { '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
	'--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M',
	'-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
	'..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '.----': '1',
	'..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7',
	'---..': '8', '----.': '9', '-----': '0', '/': ' '}

#Dictionary containing the mapping to each morse code to a letter or number as a string
morse_mapping_code = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.','F': '..-.',
	'G':'--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--',
	'N': '-.', 'O': '---',  'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
	'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',  'Z': '--..', '1': '.----',
	'2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',  '7': '--...',
	'8': '---..',  '9': '----.', '0': '-----',  ' ': '/'}
	
#Writes a line of morse code into a string_To_Morse_Code
#Takes in a fileName from where the morse code is from
def morse_Code_To_String(fileName):

	codes = generic_Read(fileName)

	code_storage = ''

	sentence_storage = ''

	for code in codes:
		print(code)
		for char in code:
			if(char == ' '):
				sentence_storage += morse_mapping_string[code_storage]
				code_storage = ''
			else:
				code_storage += char
		sentence_storage += morse_mapping_string[code_storage]
		print(sentence_storage + '\n')
		sentence_storage = ''
		code_storage = ''

#Writes a list of strings (sentence or not) into a line of morse code
#Writes to a given file name
def string_To_Morse_Code(fileName, stringList):

	full_Code = ''
	code_List = []
	upperCase = ''
	
	for string in stringList:
		upperCase = string.upper()
		
		for char in upperCase:
			full_Code += morse_mapping_code[char] + ' '
			
		if full_Code.endswith(' '):
			full_Code = full_Code[:-1]
		
		code_List.append(full_Code)
		full_Code = ''
	
	generic_Write(fileName, code_List)
	
morse_Code_To_String("morse_code.txt")

string_List_Test = ["This is a prerecorded message"]

string_To_Morse_Code("morse_string.txt", string_List_Test)

morse_Code_To_String("morse_string.txt")
			