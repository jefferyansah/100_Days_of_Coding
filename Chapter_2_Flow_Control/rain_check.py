
# def rain_checker():
# 	print('Is it raining')
# 	rain_answer = input()
# 	return rain_answer

# def umbrella_cheker():
# 	print('Do you have an umbrella')
# 	umbrella_answer = input()
# 	return umbrella_answer

####################33
print('Hey Welcome to Rain Checker App')
print('Is it raining')
rain_answer = input()


while rain_answer == 'yes':

	print('Do you have an umbrella')
	umbrella_answer = input()

	if umbrella_answer == 'no':
		print('Wait a While')
		print('....')

	else:
		print('Go Outside')
		break

	print('Is it raining')
	rain_answer = input()
	
else:
	print('Go Outside')

