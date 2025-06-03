# Soma de Números pares

numero = int(input(f'\nInsira um núvemro inteiro positivo: '))
lista = []

for i in range(1,numero+1):
    if i % 2 == 0:
        lista.append(i)
print(f'Lista dos números pares: {(lista)}')
print(f'Soma dos números pares: {sum(lista)}')
