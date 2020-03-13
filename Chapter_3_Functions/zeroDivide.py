def spam(divideBy):

	return 42 / divideBy

	

try:
	print(spam(0))
	print(spam(1))
except:
	print('You cannot divide by Zero')
