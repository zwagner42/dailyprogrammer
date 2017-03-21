#Program that writes the song "99 bottles of beers on the wall"

#1 bottle of beer on the wall, 1 bottle of beer.
#Take one down and pass it around, no more bottles of beer on the wall.

#For loop that will go backwards through the numbers 99-0
#Third argument is the incrementing value
for num_beers in range(99, -1, -1):
	num = str(num_beers)
	
	if(num_beers >= 2):
		message = ' ' + num + ' bottles of beer on the wall, ' + num + ' bottles of beer. '
		message += 'Take one down and pass it around, ' + num + ' bottles of beer on the wall.'
	elif(num_beers == 1):
		message = ' ' + num + ' bottle of beer on the wall, ' + num + ' bottle of beer. '
		message += 'Take one down and pass it around, no more bottles of beer on the wall.'
	else:
		message = ' No more bottles of beer on the wall, no more bottles of beer. ' 
		message += 'Go to the store and buy some more, 99 bottles of beer on the wall.'
		
	print(message, end='')