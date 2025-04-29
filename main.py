from classes import *

# cliente = Cliente.create(nome="Joao", telefone="7854965", endereco="wgfhegfyjwekm")
# cliente = Cliente.create(nome="Maria", telefone="7854965", endereco="wgfhegfyjwekm")
# cliente = Cliente.create(nome="Guilhermew", telefone="7854965", endereco="wgfhegfyjwekm")
# cliente = Cliente.create(nome="Joasg", telefone="7854965", endereco="wgfhegfyjwekm")
cliente = Cliente.create(nome="Joao", telefone="5555555", endereco="wgfhegfyjwekm")

a = Cliente.select().where(Cliente.nome == 'Joao')

for cliente in Cliente.select().where(Cliente.nome == 'Joao'):
    print(cliente.nome, cliente.telefone)