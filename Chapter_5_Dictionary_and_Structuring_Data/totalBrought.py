allGuests = {'Alice': {'apples':5, 'pretzels':12},
              'Bob' : {'ham': 3, 'apples':2},
              'Carol': {'cups':3, 'apple pies':1}}


def totalB(guests, item):

	numBrought = 0
	for k, v in guests.items():
		numBrought = numBrought + v.get(item, 0)
	return numBrought


print(totalB(allGuests, 'apples'))