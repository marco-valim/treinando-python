# Dicionário chamado aluno
aluno = {
    "nome": "Ana",
    "idade": 22,
    "curso": "Engenharia"
}
# Imprima o valor da chave "curso".
print(f'Valor da chave curso: {aluno["curso"]}')

# Modifique o valor da chave "idade" para 23.
aluno["idade"] = 23
print(f'Valor da chave idade: {aluno["idade"]}')

# Adicione a chave "nota_final" com valor 8.5.
aluno["nota_final"] = 8.5
print(aluno)

# Percorra o dicionário aluno e imprima cada chave e valor.
for chave, valor in aluno.items():
    print(f'Chave: {chave} | Valor: {valor}')