tarefas = []
tarefas_concluidas = []
menu = ''

while menu != '5':
    menu = str(input(f'''\n-------------MENU-------------
1 - Adicionar nova tarefa
2 - Vizualizar tarefas
3 - Vizualizar tarefas concluídas
4 - Concluir tarefa
5 - Sair do programa
                
Escolha as opções do menu: '''))

    if menu == '1':
        tarefas.append(str(input(f'Informa a tarefa a ser adicionada: ')))
        continue

    elif menu == '2':
        print(f'Lista de tarefas: {tarefas}')
        continue
    elif menu == '3':
        print(f'Lista de tarefas concluídas: {tarefas_concluidas}')
        continue
    elif menu == '4':
        concluida =  str(input(f'Informe a tarefa que deseja concluir: '))
        tarefas_concluidas.append(concluida)
        tarefas.remove(concluida)
        continue
    else:
        print('Programa encerrado\n')