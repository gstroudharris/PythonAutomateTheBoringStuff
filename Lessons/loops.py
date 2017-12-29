#Loops (for and while)

#For loops
#num is the current number in range
#range is how many times the process runs
#total keeps a running total

total = 0
for num in range(256):
    total = total + num
print(total)

#while loop
#i = the number of loops run
#while we have less than five loops run, we print our name, convert i to a string and present it

print('my name is ')
i = 0
while i < 5:
    print('Grant ' + str(i))
    i = i + 1
    
#for version of program requires a range (from, to, rate)
#The loopNumber variable uses a += shortcut for 'loopNumber = loopNumber + 1'
loopNumber = 0
for i in range(1, 15, 2):
    loopNumber += 1
    print('This loop has run ' + str(loopNumber) + ' times')
    #to make this run only one time, uncomment #break
    #break
    continue
    #to see the debug text, comment out continue
    print('are we seeing this text?')
