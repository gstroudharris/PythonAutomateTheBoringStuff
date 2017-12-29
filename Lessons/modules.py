#system level operations
#purpose: Ask the userr if they want to keep the program open with y/n
#if the user types n the program will exit
#if the user types anything else, the program will stay open

import sys

choice = ''

print('Hello, shall we exit? ')
choice = input('n... or anything else')
if choice == 'n':
    print('exiting')
    sys.exit()
else:
    print('continuing program')

#importing modules
#purpose: Import a native module and generate a random number using module.specificmodule
import random

randomNumber = random.randint(1, 100)

print('Your random number is ' + str(randomNumber))

#import a custom module with pip.exe before running pyperclip
#purpose: copy/paste a user's input

import pyperclip
input('copy some text for me to output')

print(pyperclip.paste())
