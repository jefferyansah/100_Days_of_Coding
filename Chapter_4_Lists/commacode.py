

input_list = ['Hello World', 'See', 'the', 'amazing', 'fantastic']


def comma_add(list_needed):


	printer = ''
	length_checker = len(list_needed)

	counter = 1

	for item in list_needed:


		if counter == length_checker:

			printer += ( ' and ' +str(item) )
			break
		

		else: 

			if length_checker ==2:

				printer += (str(item))

			else:
				printer += (str(item) + ', ')

		counter += 1
			
	print(printer) 

comma_add(input_list)