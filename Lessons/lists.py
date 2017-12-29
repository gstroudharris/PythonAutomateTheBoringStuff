#purpose: place items in a list, put them in a function, then call them
myLists = [['Grant', 'Dana', 'ListItem3'], [10, 20, 35]]


#index evaluates to a single item at a time
print((myLists[0][0]) + str((myLists[1][-2])))


#slice will evaluate to a a whole list
print(myLists[1:2])


#replace an item in the list
myLists[1][0] = 'replaced'
print(myLists)

#extend the list by assigning new entries
myLists[1][1:3] = ['with', 'some', 'new', 'words']
print(myLists)


#de-assign an item with del
del myLists[1][-2]
print(myLists)

#see how long a list is with len function

print(len(myLists))

#multiply the list by two and print
print(myLists * 2)

#list a str

print(list('helloooooo'))

#see if an item is in the list with 'in', or 'not in' for the opposite
searchWord = input('what word should we find in a name list? ')

print(searchWord in ['Grant', 'bagel'])
