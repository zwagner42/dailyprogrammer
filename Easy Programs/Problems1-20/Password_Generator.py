#Random Password Generator.  Limit of 50 passwords per run.  Passwords are lengths of 25 max.
#Uses numbers and alphabetic characters

from random import sample

print("\nWelcome to the random password generator!\n")

num_Passwords = input("How many passwords would you like to generate? (Limit 50): ")
len_Passwords = input("How long would you like the passwords to be? (Limit 25): ")

while(not num_Passwords.isdigit() or not len_Passwords.isdigit()):
	print("\nPlease enter the NUMBER of passwords and LENGTH of the passwords you would like.")
	num_Passwords = input("How many passwords would you like to generate? (Limit 50): ")
	len_Passwords = input("How long would you like the passwords to be? (Limit 25): ")
	
num_Passwords = int(num_Passwords)
len_Passwords = int(len_Passwords)

for num in range(0, num_Passwords):
	print(''.join(sample("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", len_Passwords)))

