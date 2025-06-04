lista = [1, 2, 5, 3, 4, 5, 6, 7, 8, 9, 10]

posicao = int(input(f'''\nLista: {lista}
Infome o valor na lista para remover o valor: '''))


lista.remove(posicao)
print(f'\nLista atualizada {lista}\n')