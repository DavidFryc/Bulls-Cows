"""
projekt_2.py: druhy projekt do Engeto Online Python Akademie
author: David Fryc
email: df@emd.dk
discord: David F.#2019
"""

import os
import time
import random
from random import choice
os.system('cls')

print ('''
Hi there!
-----------------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game. 
-----------------------------------------------
''')

# RANDOM NUMBER
secret_number = random.sample(range(10), 4)

for first_zero in secret_number:
    if secret_number[0] ==0:
        random.shuffle(secret_number)

secret_int = ''
for element in secret_number:
    secret_int += str(element)

# VARIABLES
separator = ('-----------------------------------------------')
game_on = True
start=time.time()
guessed = []
first_zero = []
too_long = []
too_short = []
non_digits = []
duplicates = []
cows = 0
bulls = 0

display_number = input ('Do you want to see the secret number before guessing? Y/N: ')
if display_number == 'Y'.casefold():
    print ('Coward, the secret number is: ', secret_int)
    print ('You can always quit the game by pressing "q".')
else:
    print('No help? So proud of you!!')
    print('You can always quit the game by pressing "q".')
    separator

# CHECK, IF THE NUMBER HAS 4 SYMBOLS, DOES NOT START WITH 0 OR IS NOT STR. 
while game_on:
    number = input('Enter a number: ')
    print (separator)
    if number == 'q':
        game_on = False
        end1=time.time()
        print('Coward, you gave it up in', round(end1-start, 2), 'seconds after', len(guessed)+\
            len(first_zero)+len(too_long)+len(too_short)+len(non_digits), 'attempt(s)')
        print('The secret number was:', secret_int)
        print(separator)
    elif not number.isdigit():
        print('Sorry, you need to enter a number...')
        print ('Already guessed numbers:', ', '.join(guessed))
        print(separator)
        non_digits.append(number)
    elif len(number) > 4:
        print('Sorry, the number is too long...')
        print ('Already guessed numbers:', ', '.join(guessed))
        print(separator)
        too_long.append(number)
    elif len(number) < 4:
        print('Sorry, the number is too short...')
        print ('Already guessed numbers:', ', '.join(guessed))
        print(separator)
        too_short.append(number) 
    elif len(set(number)) != 4:
        print('Sorry, the number can not contain duplicates...')
        print ('Already guessed numbers:', ', '.join(guessed))
        print(separator)
        duplicates.append(number)
    elif int(number[0]) == 0:
        print('Sorry, the first number can not be zero...')
        print ('Already guessed numbers:', ', '.join(guessed))
        print(separator)
        first_zero.append(number)

# CHECK, IF THE GUESSED NUMBER WAS ALREADY GUESSED:        
    else:
        if number not in guessed:
            guessed.append(number)
            print ('Already guessed numbers:', ', '.join(guessed))
            print(separator)

        else:
            print ('This number was already guessed.')
            print ('Already guessed numbers:', ', '.join(guessed))
            print(separator)

# CALCULATING COWS:
        if int(number[0]) in secret_number:
            cows +=1
        if int(number[1]) in secret_number:
            cows +=1
        if int(number[2]) in secret_number:
            cows +=1
        if int(number[3]) in secret_number:
            cows +=1

# CALCULATING BULLS:
        if int(number[0]) == secret_number[0]:
            cows -=1
            bulls +=1
        if int(number[1]) == secret_number[1]:
            cows -=1
            bulls +=1
        if int(number[2]) == secret_number[2]:
            cows -=1
            bulls +=1
        if int(number[3]) == secret_number[3]:
            cows -=1
            bulls +=1

# FINISH AFTER ALL BULLS WERE IDENTIFIED   
        if bulls == 4 and display_number == 'y'.casefold():
            print('Yeah, the number is correct! But you saw the number at the beginning.')
            end2=time.time()
            #print (round(end2-start, 2))
            print('You needed', len(guessed)+len(first_zero)+len(too_long)+len(too_short)\
                +len(non_digits)+len(duplicates),'attempt(s) and', round(end2-start, 2),'seconds.')
            game_on = False
        
        elif bulls == 4:
            print('Congratulations, you won with no help!'.upper())
            end2=time.time()
            #print (round(end2-start, 2))
            print('You guessed the right number in'.upper(), len(guessed)+len(first_zero)+len(too_long)+len(too_short)\
                +len(non_digits)+len(duplicates),'attempt(s) and'.upper(), round(end2-start, 2),'seconds.'.upper())
            game_on = False
        
        print('Bulls: ', bulls, 'Cows: ', cows)
        print(separator)
        cows = 0
        bulls = 0