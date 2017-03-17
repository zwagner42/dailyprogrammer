//Text Adventure Game in C.  Compile with gcc not g++.

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <time.h>

typedef enum { false, true } bool;

//Death message
#define DEATH "\nYou died!  Your journey ends here\n"

//Used to get user input when a single digit number is needed
//msg is the message shown to the user
//errMSG is the error message shown in the case of invalid input
int user_Input(char *msg, char * errMSG);
int main_Menu();
int adventure();

int main()
{
	//Reset seed for random numbers
	srand(time(NULL));
	//Variables used for looping Main Menu
	bool test = false;
	int choice = 0;
	
	while(test == false)
	{
		choice = main_Menu();
		if(choice == 1)
		{
			test = true;
		}
	}
	
	printf("\nThank you for playing!");
	
	return 0;
}

int main_Menu()
{
	//Counter for number of times you choose the right door
	int counter = 0;
	
	//Main Menu Message
	printf("\nWelcome to the Short Text Adventure!");
	printf("\n1. Start the Game");
	printf("\n2. Exit the Game");
	
	//Get User's Choice
	int choiceMenu = user_Input("\nEnter your choice (1 or 2): ", "\nPlease choose a valid option.\n");
	
	//Conditionals for User's Choice
	if(choiceMenu == 1)
	{
		printf("\nYou wake up in a room with only two doors.\n\nWhich door will you choose?");
		counter = adventure();
		printf("\nYou survived %d rounds!", counter);
		return 0;
	}
	else if(choiceMenu == 2)
	{
		return 1;
	}
	else
	{
		return 0;
	}
}

//Gets user input for a one-digit positive integer
int user_Input(char * msg, char * errMSG)
{	
	//Used for input checking
	char ch;
	//Buffer of 25 characters
	char storage[1];
	
	printf(msg);
	fgets(storage, 2, stdin);
	
	if(isdigit(*storage) == 0)
	{
		//Used to clear buffer
		while((ch = getchar()) != EOF && ch != '\n')
		{}
	
		printf(errMSG);
		return -1;
	}
	
	//Used to clear buffer
	while((ch = getchar()) != EOF && ch != '\n')
		{}
	
	return atoi(storage);
}

//Function running the adventure.
//The adventure has you choose between 2 doors where one will randomly kill you.
//You keep going until you die.
int adventure()
{
	//Counter for tracking number of right choices
	int counter = 0;
	
	//User selection
	int choice_Adventure = -1;
	
	//Limit random number to 1 and 2
	int random_number = (rand() % 2) + 1;
	
	//Menu for the base adventure
	printf("\n1. Right");
	printf("\n2. Left");
	choice_Adventure = user_Input("\nEnter your choice (1 or 2): ", "\nPlease choose a valid option.\n");
	
	//Conditionals for the choices
	if(choice_Adventure == -1)
	{
		printf("\nYou seem undecisive.  Remember that there are two doors in front of you\n");
		adventure();
	}
	else if(choice_Adventure == 1)
	{
		if(random_number == choice_Adventure)
		{
			printf(DEATH);
			return counter;
		}
		else
		{
			printf("\nYou see two more doors!");
			counter++;
			counter += adventure();
		}
	}
	else if(choice_Adventure == 2)
	{
		if(random_number == choice_Adventure)
		{
			printf(DEATH);
			return counter;
		}
		else
		{
			printf("You see two more doors!");
			counter++;
			counter += adventure();
		}
	}
	
	return counter;
}