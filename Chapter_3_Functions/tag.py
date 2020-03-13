import random


genNum = random.randint(1,20)
print('I am thinking of a number between 1 and 20...The secret number is: ' + str(genNum))

def checker():


	print('Take a guess')
	guessNum = int(input())

	while True:

		i = 1


		if guessNum > genNum:

			print('Your guess is too High')

		elif guessNum < genNum:

			print('Your guess is too Low')

		elif guessNum == genNum:
			print('Good Job. You guessed my number in ' + str(i) + ' guesses')
			break

		i = i + 1


checker()