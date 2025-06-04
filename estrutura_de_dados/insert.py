posicao = int(input(f'\nInfome a posição para inserção: '))
valor = int(input(f'Informe o valor a ser inserido: '))
lista = [1, 2, 3, 4, 5]

lista.insert(posicao, valor)
print(f'Lista atualizada {lista}\n')