name  = ''
while name != 'your name':
	print('Please type your name')
	name = input()
print('Thank you')



#Another Version using break Statement

while True:
	print('Please type your name')
	name  = input()
	if name == 'your name':
		break
print('Thank you')