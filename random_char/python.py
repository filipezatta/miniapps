import random
randomlist = []
for i in range(0,8):
    n = random.randint(0,1)
    randomlist.append(n)

x = list(map(lambda x: str(x), randomlist))    
x = ''.join(x)

print(x)
#x = "00100101"

print(chr(int(x[:8], 2)))

