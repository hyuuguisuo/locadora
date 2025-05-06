from classes import *
import os

print("============ VIDEOLOCADORA ============")

opcao = True

while(opcao != False):
    os.system("cls")

    print("---------------- MENU ----------------")
    print("[1] - Cadastrar cliente.")
    print("[2] - Buscar cliente.")    
    print("[3] - Excluir cliente.")   
    print("[4] - Cadastrar filme.")
    print("[5] - Verificar devolução de filmes.")
    print("[6] - Verificar quantidade de filmes alugados.")
    print("[0] - SAIR\n")

    opcao = int(input("Digite a opção desejada:\n"))
    
    if (opcao == 0):
        opcao = False

    elif (opcao == 1):
        print("----------------------------------")
        nome_cli = input("Digite o nome do cliente:\n -> ")
        telefone_cli = input("Digite o telefone do cliente:\n -> ")
        endereco_cli = input("Digite o endereco do cliente:\n -> ")

        cliente = Cliente.create(nome = nome_cli, telefone = telefone_cli, endereco = endereco_cli)

    elif (opcao == 2):
        id_cli = int(input("Digite o número de registro do cliente:\n -> "))

        for c in Cliente.select().where(Cliente.id == id_cli):
            print(f" -> | {c.nome}")
        
    elif (opcao == 3):
        id_cli = int(input("Digite o número de registro:\n -> "))
       #Aqui a gente cria um método fornecido pelo Peewee, isso é basicamente uma consulta que verifica se existe algum registro na tabela Cliente que satisfaça a condição
       #Cliente.id==id_cli,assim retornando um valor booleano. Em resumo: ele verifica  se há a existência de registro correspondente em uma determinada consulta no banco de dados

        cliente_existe = Cliente.select().where(Cliente.id == id_cli).exists()
        #Se o método acima retornar o valor True, então a condição do if vai ser satisfeita e os processos vão acontecer
        if cliente_existe:
            #get_by_id(id_cli)  faz a busca de um único registro na tabela desejada(Que no caso seria a nossa classe Cliente), que corresponda ao valor passado como argumento
            #(Sendo o valor que o usuário digitou). Caso o registro desejado for encontrado, ele pega a linha e os atributos (coluna)  e cria um novo objeto
            #sendo ele uma instância da classe. Após isso, os valores das colunas do banco de dados daquele registro preencherá os atributos do objeto.
            #No final , esse método vai retornar o objeto criado (com todos os valores sendo acessíveis )
            cliente=Cliente.get_by_id(id_cli)
            #Aqui ele vai deletar essa instância
            cliente.delete_instance()
            print(f" o Cliente {cliente.nome} foi excluído ")
        else:

             print(f"Não existe o número de registro {id_cli}")

    elif (opcao == 4):
        print("----------------------------------")
        titulo_filme= input("Digite o título do filme:\n -> ")
        ano_lancamento_filme= input("Digite o ano de lançamento do filme:\n -> ")
        diretor_filme = input("O nome do diretor:\n -> ")
        duracao_minutos_filme = input("...e a duração total do filme (minutos):\n -> ")

        filme = Filme.create(titulo = titulo_filme, ano_lancamento = ano_lancamento_filme, diretor = diretor_filme, duracao_minutos = duracao_minutos_filme)

    #input("\nAperte ENTER para continuar (...)")
    elif(opcao==5):
        titulo_filme = input("Digite o nome do filme:\n -> ")
        devolucao=Filme.select().where(Filme.titulo==titulo_filme).exists()
        
         
          
