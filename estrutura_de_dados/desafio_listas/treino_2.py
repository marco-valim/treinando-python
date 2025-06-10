# Soma e média de números
numeros = [7, 4, 9, 2, 6]

soma = sum(numeros)
print(f'''Soma dos números: {soma}
Média dos números: {soma / len(numeros)}''')

# Nova lista apenas com os números pares da lista acima.
numeros_pares = []
for numero in numeros:
    if numero % 2 ==0:
        numeros_pares.append(numero)
print(f'Números pares: {numeros_pares}')

# O quadrado de cada número.
lista_quadrado = []
for quadrado in numeros:
    quadrado **= 2
    lista_quadrado.append(quadrado)
print(f'Valor quadrado de cada número: {lista_quadrado}')

# Apenas os valores maiores que 3.
lista_maior_3 = []
for maior_3 in numeros:
    if maior_3 > 3:
        lista_maior_3.append(maior_3)
print(f'Números maiores que 3: {lista_maior_3}')
