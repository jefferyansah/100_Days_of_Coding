

import copy
spam = [1, 2, 3]
def eggs(someParameter):
	#someParameter = copy.copy(someParameter)
	someParameter.append('Hello')

	#print(someParameter)



eggs(spam)
print(spam)