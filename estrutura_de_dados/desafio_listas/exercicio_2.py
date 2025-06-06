numeros = [10, 23, 45, 67, 81, 90, 3, 12, 55, 78]
pares = []
maiores_que_50 = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    elif numero > 50:
        maiores_que_50.append(numero)

print(f'\nLista de números pares: {pares}')
print(f'Lista de números maior que 50: {maiores_que_50}\n')