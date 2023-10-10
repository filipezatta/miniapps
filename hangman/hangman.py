import os
os.system('cls' or 'clear')
hangmanart = ["  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========", 

        "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========", 

        "  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n========="]
#credit https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c


#print(hangmanart[-1])

word = list(input("Enter a word: "))
numchars = len(word)

print(len(list(word)))


input('EOF')
os.system('cls' or 'clear')
