
birthdays = {'Jeff': '12 Feb', 'Robyn': '7 March', 'Sandra':'25th Aug'}


while True:
	name = input('Enter a name: ')
	if name == '':
		break

	if name in birthdays:
		print(birthdays[name] + " is the birthday of " + name)
		break

	else:
		print('I dont have the birthday information for ' +  name)
		bday = input('What is their birthday: ')
		birthdays[name] = bday
		print('Thanks for the info, I have updated my Database with ' + name + "'s information")
		break

		# I added my own Code

# for person, date  in birthdays.items():


if 'Robyn' in birthdays.keys() and '7' in birthdays.values():
	print('You just won the lottery. Is your Lucky day, ' + person)

else:
	print('We dont have a winner yet')