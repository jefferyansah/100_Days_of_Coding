def spam():

	global eggs
	eggs = 'spam'

def bacon():
	eggs = 'bacon'

def ham():
	print(eggs)

eggs = 43
spam()
print(eggs)