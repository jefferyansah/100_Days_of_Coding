
# while True:

# 	print('Who are you')
# 	name = input()
# 	if name != 'Joe':
# 		continue
# 	print('Hello, Joe, Whats your password')
# 	password = input()
# 	if password == 'swordfish':
# 		break
# print('Access Granted')


#Another way to execute it
fname = ''
while not fname:
	print('Who are you')
	name = input()
	if name == 'Joe':
		print('Hello, Joe, Whats your password')
	else:
		continue
	password = input()
	if password != 'swordfish':
		continue
	else:
		break
print('Access Granted')