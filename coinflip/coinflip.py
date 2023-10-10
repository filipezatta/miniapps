import random
import os
import sys

os.system('cls' or 'clear')

yes = ['yes', 'sim', 'y', 's', "True", "true"]
no = ['no', 'nao', 'n', 'não', "false", "False"]

def coinflip():
    num = int(input('how many times do you want to flip the coin? '))
    count = 0
    tails = 0
    heads = 0
    while True:
        coin_flip = random.randint(1,2)
        
        if count == num:
            break

        if coin_flip == 1:
            #print('Heads')
            heads+=1

        elif coin_flip == 2:
            #print("Tails")
            tails+=1
        
        count+=1
    print(f'heads: {heads}\ntails: {tails}')
    if input('play again?') in yes:
        coinflip()
    else:
        os.system('cls' or 'clear')
        sys.exit()

coinflip()

