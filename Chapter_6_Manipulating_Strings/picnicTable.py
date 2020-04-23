
def printPicnic(itemsDict, leftWidth, rightWidth):

    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))

    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))


picnic_items = {'sandwiches': 4, 'apples':12, 'cups':4, 'cookies': 8000}
printPicnic(picnic_items, 12, 5)
printPicnic(picnic_items, 20, 6)