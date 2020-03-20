
pet_list = ['Jake', 'Corona', 'Wuhan']
pet_list = [i.lower() for i in pet_list]
pet_name = str(input('Enter a pet name: ' )).lower()

if pet_name in pet_list:
	print('Yea there is a pet called ' + pet_name )

else:
	print('Sorry ' +  pet_name +  ' is not a pet here')