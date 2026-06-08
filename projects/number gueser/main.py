import random

a = random.randint(1,25)
guesses = 0

while True:
    num = int(input('write a no : '))
    if num == a:
        guesses = guesses + 1
        print('correct number 😁')
        print(f'you took {guesses} guesses .')
        break
    elif num > a:
        guesses += 1
        print(f'number is low than {num}')
    elif num < a:
        guesses += 1
        print(f'number is high than {num}')
    else:
        print('choose else')