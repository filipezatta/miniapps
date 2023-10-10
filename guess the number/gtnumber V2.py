import random 
import os
import sys
os.system('cls' or 'clear')
yes = ['yes', 'sim', 'y', 's', "True", "true"]
no = ['no', 'nao', 'n', 'não', "false", "False"]

def randomghnumber():
    number = random.randint(1,10)
    print(number)
    while True:
        if int(input('guess a number between 1 and 10 ')) == number:
            print(number)
            print(f'you won, the number was {number}')
            break
    
    os.system('cls' or 'clear')
    playagain()
    
    
def ghnumber():
    number = input('choose a number between 1 and 10 \n')
    os.system('cls' or 'clear')
    numcheck = 0
    while numcheck != number:
        numcheck = input('guess a number between 1 and 10 ')
            
    print(f'you won, the number was {number}')
    playagain()

def playagain():
    if input('play again?') in yes:
        if input('random or choose number? \n') == 'random':
            randomghnumber()
        else:
            ghnumber()  
    else:
        os.system('cls' or 'clear')
        sys.exit()

if input('random or choose number? \n') == 'random':
    randomghnumber()
else:
    ghnumber()