# Verifique a Existência de uma Chave
contatos = {
    "João": 65234789,
    "Maria": 98765432,
    "Pedro": 12345678,
    "Ana": 785219635,
    "Rute": 78541236
}

for contato in contatos:
    if contato == "Maria":
        print(f'O contado {contato} existe na lista')
    else:
        print(f'O contato {contato} não existe na lista')