#Get the name, age, and reddit username by command line input
#Then write the information to a file called log.txt


name = input("Enter your Name: ")

age = input("Enter your Age: ")

username = input("Enter your Reddit Username: ")

message = "Your name is " + name + ", you are " + age + ", and your reddit username is " + username
print(message)

target = open("log.txt", "a")

target.write(message)
target.write('\n')

target.close()