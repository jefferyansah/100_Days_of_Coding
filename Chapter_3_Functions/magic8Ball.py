
import random


def getAnswer(ansNumber):

	if ansNumber == 1:

		return "'It's certain"

	elif ansNumber == 2:

		return "It is decidedly so"

	elif ansNumber == 3:

		return "IReply I dont know"

	elif ansNumber == 4:

		return "Hurray, we won"

	elif ansNumber == 5:

		return "Charlie Whatsapp"


#number = random.randint(1,5)
print('Type a number')
#number  = int(input())
print(getAnswer(int(input())))
#print(fortune)

