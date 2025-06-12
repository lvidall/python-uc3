dicinario = {
    'nome': 'Luis',
    'cpf': '12657-23',
    'telefone': '2499999'
}
dicinario['senha'] = 12346
print(dicinario)

dicinario.update({'telefone'':''249898989'})
print(dicinario)

del dicinario['telefone']
print(dicinario)
