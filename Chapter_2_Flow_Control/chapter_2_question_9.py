
import random

#Solution 1
# while True:
# 	print('Greetings!')
# 	spam  = input()
# 	if spam == '1':
# 		print('Hello')
# 		break

# 	elif spam == '2':
# 		print('Howdy')
# 		break

#Solution 2

while True:
	spam = str(random.randint(0,5))
	print(spam)
	print('Greetings')

	if spam == '1':
		print('Hello')
		break

	elif spam == '2':
		print('Howdy')
		break