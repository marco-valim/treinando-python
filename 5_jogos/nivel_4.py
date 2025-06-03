# Jogo de adivinhar o número

import random

numero_pensado = random.randint(1,100)

for i in range(7):
    print(f'\nTente adivinhar o número entre 1 e 100. Você tem {7-i} tentativas.')
    numero_informado = int(input(f'Informe um número inteiro positivo: '))
    if numero_informado > numero_pensado:
        print(f'Muito alto! Tente novamente.')
    elif numero_informado < numero_pensado:
        print(f'Muito baixo! Tente novamente.')
    elif numero_informado == numero_pensado:
        print(f'Parabéns! Você acertou o número {numero_pensado} em {i} tentativas!\n')
        break
    else:
        print(f'Que pena! Você não conseguiu adivinhar. O número era {numero_pensado}.\n')