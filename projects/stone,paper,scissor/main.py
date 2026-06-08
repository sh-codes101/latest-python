

# A SIMPLE | STONE | PAPER | SCISSOR | GAME . . . 🤩🤩



import random

score = 0

s = 'scissor'
p = 'paper'
st = 'stone'

comp = [s,p,st]
sure = input('are you sure you wanna play ( y/n ) : ')
print('''HERE ARE THE SHORTFORMS :
           S = SCISSOR
           P = PAPER
           ST = STONE
     ''')

while True:
    if sure == 'n':
         break
    elif sure == 'y':
        ch = random.choice(comp)
        pl = input('write your choice : ')
        if (ch == s and pl == 's'):
            print('draw')
            print(f'score: {score}')
        elif (ch == p and pl == 'p'):
            print('draw')
            print(f'score: {score}')
        elif (ch == st and pl == 'st'):
            print('draw')
            print(f'score: {score}')
        elif (ch == s and pl == 'st'):
            print('player wins')
            score = score + 1
            print(f'score : {score}')
        elif (ch == p and pl == 's'):
            print('player win')
            score = score + 1
            print(f'score: {score}')
        elif (ch == st and pl == 'p'):
            print('player wins')
            score = score + 1
            print(f'score: {score}')
        elif (ch == s and pl == 'p'):
            print('computer wins')
        elif (ch == p and pl == 'st'):
            print('computer wins')
        elif (ch == st and pl == 's'):
            print('computer wins')
    else:
        print('invalid option ...')