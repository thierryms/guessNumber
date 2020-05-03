#Jogo de advinhar um número

import random

jogador = random.randint(1,3)
if jogador == 1:
    print('Thierry começa!')
elif jogador == 2:
    print('Sulamita começa!')
else:
    print('Bebelly começa!')
secretNumber = random.randint(1,25)
print('Im thinking of a number between 1 and 100')

for guessTaken in range(20):
    print('Take a guess')
    guess = int(input())

    if guess <  secretNumber:
        print('Your number is too low!')
    elif guess > secretNumber:
        print('Your number is too high!')
    else:
        print('Congratulations, you take the right number!!!!')

if guess == secretNumber:
    print('Você errou ' + str(guessTaken) +  ' vezes antes de acertar!' )

else:
    print('Você não conseguiu acertar, o número secreto era: ' + str(secretNumber))




