import random


genNum = random.randint(1,20)
print('I am thinking of a number between 1 and 20...The secret number is: ' + str(genNum))

def checker():


	
	#Let the user get only 6 times
	for num in range(1,7):



		try:

			print('Take a guess')
			guessNum = int(input())
			

			if guessNum > genNum:

				print('Your guess is too High')
				
				

			elif guessNum < genNum:

				print('Your guess is too Low')


			else:
				print('Good Job. You guessed my number in ' + str(num) + ' guesses')

				break
		except:
			print('You entered a string, Try again')
	# if guessNum == genNum:
	# 	print('Good Job. You guessed my number in ' + str(num) + ' guesses')

	#else:
	if guessNum != genNum:
		print('Nope the Number I was thinking was ' + str(genNum))

			

	
checker()

########################33
# Let's try and break this down into functions etc
"""
What do we need:
A print statement for the intro

A function to check the condition


A function to  present the final answer


"""
