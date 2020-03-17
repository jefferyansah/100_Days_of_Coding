

numOfCats= int(input('How Many cats do you have?:  '))

catID =1
cat_name_list = []

for i in  range (numOfCats):

	catNames = input('Enter the name of Cat Number ' +  str(catID)+  ': ')
	#print(catNames)
	cat_name_list = cat_name_list + [catNames]
	#print(cat_name_list)
	catID = catID + 1
print('The name of your cats are:')
for name in cat_name_list:
	print(name)



