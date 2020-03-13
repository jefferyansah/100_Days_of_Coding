

def spam():

	

	eggs = 'spam local'
	print(eggs)
	return eggs


def bacon():
	eggs = 'bacon local'
	print(eggs)
	spam()
	print(eggs)


eggs = 'global'
bacon()
print(eggs)
