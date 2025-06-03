# Verificador de idade de votação

nome = input(f'\nInforme seu nome: ')
idade = int(input(f'Informe sua idade: '))

IDADE_MIN_VOTAR = 16

if idade >= IDADE_MIN_VOTAR:
    print(f'{nome}, você pode votar!\n')
else:
    print(f'{nome}, você não pode votar!\n')