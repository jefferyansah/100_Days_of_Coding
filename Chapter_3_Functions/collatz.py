


def collatz(number):

	

	if  number%2 ==0:
		a = number//2
		return print(a), a

	elif number%2 !=0:
		a =  3 * number + 1
		return print(a), a

		

print('Enter a number')
vra = int(input())







# while a != 1:
# 	collatz(vra)
