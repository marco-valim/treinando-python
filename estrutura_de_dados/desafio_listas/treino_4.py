# Crie uma lista chamada alunos com 3 dicionários
alunos = [
    {"nome": "Maria", "idade": 20, "nota": 7.5},
    {"nome": "Marta", "idade": 25, "nota": 8.7}, 
    {"nome": "Jonas", "idade": 28, "nota": 5.5}
]

# Conta a quanditade de alunos
soma_notas = 0
quantidade_alunos = len(alunos)

# Faz a soma das notas
for alunos in alunos:
    soma_notas += alunos["nota"]

# Calcula a média das notas
media = soma_notas / quantidade_alunos
print(f'\nA media é: {media:.2f}\n')