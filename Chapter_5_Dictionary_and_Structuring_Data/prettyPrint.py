import pprint

message = 'The outbreak of this pandemic is a disaster because the sudden turn of  this events is not something good.'
list1 = [word for word in message.lower().split()]
count = {}

for i  in list1:
	count.setdefault(i, 0)
	count[i] = count[i] + 1

pprint.pprint(count)
print(pprint.pformat(count))