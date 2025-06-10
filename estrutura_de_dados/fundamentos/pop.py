lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

while True:
    position = int(input(f'\nInforme a posição para remover: '))
    lista.pop(position)
    print(f'\nLista atualizada {lista}\n')