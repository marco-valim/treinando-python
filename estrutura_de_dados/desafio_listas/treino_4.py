# Crie uma lista chamada alunos com 3 dicionários
alunos = [
    {"nome": "Maria", "idade": 20, "nota": 7.5},
    {"nome": "Marta", "idade": 25, "nota": 8.7}, 
    {"nome": "Jonas", "idade": 28, "nota": 5.5}
]
lista_aprovados = []
soma_notas = 0

# Conta a quanditade de alunos
quantidade_alunos = len(alunos)

# Faz a soma das notas
for aluno in alunos:
    soma_notas += aluno["nota"]

# Calcula a média das notas
media = soma_notas / quantidade_alunos
print(f'\nA media é: {media:.2f}\n')

# Lista com apenas os alunos que têm nota >= 7
for aluno in alunos:
    if aluno["nota"] >= 7:
        lista_aprovados.append(aluno["nome"])  
print(f'Alunos aprovados: {lista_aprovados}\n')

# Ordene a lista alunos da maior para a menor nota.
alunos.sort(key=lambda aluno: aluno["nota"], reverse=True)
print('Alunos ordenados pela maior nota: ')
for aluno in alunos:
    print(f'{aluno["nome"]} - {aluno["nota"]}')