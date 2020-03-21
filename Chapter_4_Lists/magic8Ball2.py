

import random

spam = ['It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']

#number  = int(input('Enter a Number: '))

def get_index(list_items):
	
    # index_list = []
    # for item in list_items:
    # 	idx = spam.index(item)
    # 	index_list.append(idx)
    # print(index_list)

    while True:

    	number  = int(input('Enter a Number: '))


    	if number in range(len(spam)-1):

    		print('You have entered : ' + str(number)+ ', Hence: ' + spam[number])
    		break

    	else:
    		print('Try Again')

    



get_index(spam)