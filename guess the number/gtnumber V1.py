
import os
import sys
os.system('cls' or 'clear')
yes = ['yes', 'sim', 'y', 's', "True", "true"]
no = ['no', 'nao', 'n', 'não', "false", "False"]
def ghnumber():
    if input('want to choose a number between 1 and 10 \n') in yes:
        number = input('choose a number between 1 and 10 \n')
        os.system('cls' or 'clear')
        numcheck = 0
        while numcheck != number:
            numcheck = input('guess a number between 1 and 10 ')
            
        print(f'you won, the number was {number}')
    else:
        os.system('cls' or 'clear')
        sys.exit()
ghnumber()

if input('play again?') in yes:
    ghnumber()
else:
    os.system('cls' or 'clear')
    sys.exit()


