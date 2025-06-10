# Crie uma lista chamada nomes com 5 nomes de pessoas.
nomes = ["maria", "joao", "ana", "pedro", "miguel"]

#Imprima o primeiro e o último nome da lista.
print(nomes[0], nomes[4])

# Troque o terceiro nome da lista por "Lucas".
nomes[2] = "lucas"
print(nomes)

# Adicione "Vitor" ao final da lista. / Remova o segundo nome.
nomes.append("vitor")
nomes.pop(1)
print(nomes)

# Ordene a lista em ordem alfabética. / Inverta a ordem da lista.
nomes.sort()
print(nomes)
nomes.sort(reverse=True)
print(nomes)