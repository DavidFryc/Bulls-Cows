"""
projekt_2.py: druhy projekt do Engeto Online Python Akademie
author: David Fryc
email: df@emd.dk
discord: David F.#2019
"""

import os
import time
from random import choice
os.system('cls')

print ('''
Hi there!
-----------------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game. You can always quit the game by pressing "q".
-----------------------------------------------
''')

# RANDOM NUMBER AS LIST:
start = time.time()
numbers = list(range(1, 10))
secret1 = choice(numbers)
numbers.remove(secret1)
numbers.append(0)
secret2 = choice(numbers)
numbers.remove(secret2)
secret3 = choice(numbers)
numbers.remove(secret3)
secret4 = choice(numbers)
secret_list = [secret1, secret2, secret3, secret4]

# CONVERTS LIST TO ONE NUMBER
secret_int = ""
for element in secret_list:
    secret_int += str(element)

separator = ('-----------------------------------------------')
game_on = True
guessed = []
first_zero = []
too_long = []
too_short = []
non_digits = []
cows = 0
bulls = 0

display_number = input ('Do you want to see the secret number before guessing? Y/N: ')
if display_number == 'Y'.casefold():
    print ('Coward, the secret number is: ', secret_int)
else:
    print('No help? So proud of you!!')
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
        print(separator)
    elif not number.isdigit():
        print('Sorry, you need to enter a number...')
        print ('Already guessed numbers:', ', '.join(guessed))
        print(separator)
        non_digits.append(number)
    elif int(number[0]) == 0:
        print('Sorry, the first number can not be zero...')
        print ('Already guessed numbers:', ', '.join(guessed))
        print(separator)
        first_zero.append(number)
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
        if int(number[0]) in secret_list:
            cows +=1
        if int(number[1]) in secret_list:
            cows +=1
        if int(number[2]) in secret_list:
            cows +=1
        if int(number[3]) in secret_list:
            cows +=1

# CALCULATING BULLS:
        if int(number[0]) == secret1:
            cows -=1
            bulls +=1
        if int(number[1]) == secret2:
            cows -=1
            bulls +=1
        if int(number[2]) == secret3:
            cows -=1
            bulls +=1
        if int(number[3]) == secret4:
            cows -=1
            bulls +=1

# FINISH, AS SOON AS ALL BULLS ARE IDENTIFIED   
        if bulls == 4 and display_number == 'y'.casefold():
            print('Yeah, the number is correct! But you saw the number at the beginning.')
            end2=time.time()
            #print (round(end2-start, 2))
            print('Despite that you needed', len(guessed)+len(first_zero)+len(too_long)+len(too_short)\
                +len(non_digits),'attempts', round(end2-start, 2),'and seconds.')
            print('')
            print('Real heros do it without help'.upper())
            print('')
            break
        
        elif bulls == 4:
            print('Congratulations, you won!'.upper())
            end2=time.time()
            #print (round(end2-start, 2))
            print('You guessed the right number in'.upper(), len(guessed)+len(first_zero)+len(too_long)+len(too_short)\
                +len(non_digits),'attempt(s) and'.upper(), round(end2-start, 2),'seconds.'.upper())
            game_on = False
        
        print('Bulls: ', bulls, 'Cows: ', cows)
        print(separator)
        cows = 0
        bulls = 0