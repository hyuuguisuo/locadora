from código.classes_database import *
from código.classe_logica import *

import os


                                                   # Métodos #
def cadastrarCliente():
    print("---------- CADASTRAR CLIENTE -----------\n")

    nome_cli = input("Digite o nome do cliente:\n -> ")
    telefone_cli = input("Digite o telefone do cliente:\n -> ")
    endereco_cli = input("Digite o endereco do cliente:\n -> ")

    cliente = Cliente.create(nome = nome_cli, telefone = telefone_cli, endereco = endereco_cli)

    print(f"Cliente cadastrado com sucesso!")
    print(cliente)


def buscarCliente():
    print("----------- BUSCAR CLIENTE -----------\n")

    id_cli = int(input("Digite o número de registro do cliente:\n -> "))

    for c in Cliente.select().where(Cliente.id == id_cli):
        print(f" -> | {c}")


def excluirCliente():
    print("---------- EXCLUIR CLIENTE ----------\n")

    id_cli = int(input("Digite o número de registro:\n -> "))
    
    # Aqui a gente cria um método fornecido pelo Peewee, isso é basicamente uma consulta que verifica se existe algum registro na tabela Cliente que satisfaça a condição
    # Cliente.id==id_cli,assim retornando um valor booleano. Em resumo: ele verifica  se há a existência de registro correspondente em uma determinada consulta no banco de dados

    cliente_existe = Cliente.select().where(Cliente.id == id_cli).exists()

    # Se o método acima retornar o valor True, então a condição do if vai ser satisfeita e os processos vão acontecer

    if cliente_existe:

        # get_by_id(id_cli)  faz a busca de um único registro na tabela desejada(Que no caso seria a nossa classe Cliente), que corresponda ao valor passado como argumento
        # (Sendo o valor que o usuário digitou). Caso o registro desejado for encontrado, ele pega a linha e os atributos (coluna)  e cria um novo objeto
        # sendo ele uma instância da classe. Após isso, os valores das colunas do banco de dados daquele registro preencherá os atributos do objeto.
        # No final , esse método vai retornar o objeto criado (com todos os valores sendo acessíveis )

        cliente=Cliente.get_by_id(id_cli)
        
        # Aqui ele vai deletar essa instância
        
        cliente.delete_instance()
        
        print(f" o Cliente {cliente.nome} foi excluído.")
    else:
        print(f"Não existe nenhum registro equivalente à [ {id_cli} ].")


def cadastrarFilme():
    print("----------- CADASTRAR FILME -----------\n")

    titulo_filme= input("Digite o título do filme:\n -> ")
    ano_lancamento_filme= input("Digite o ano de lançamento do filme:\n -> ")
    diretor_filme = input("O nome do diretor:\n -> ")
    duracao_minutos_filme = input("...e a duração total do filme (minutos):\n -> ")

    filme = Filme.create(titulo = titulo_filme, ano_lancamento = ano_lancamento_filme, diretor = diretor_filme, duracao_minutos = duracao_minutos_filme)

    print("Filme criado com sucesso!")
    print(filme)

def verificarDevolucao():
    ## nao existe ainda as devoluções então deixa quieto por enquanto

    print("-------- VERIFICAR DEVOLUÇÃO --------\n")

    registro= int(input("Digite o id da locação a  ser verificado:\n -> "))
    devolucao = Locacao.get_or_none(Locacao.id==registro)
    if(devolucao):
        if(devolucao.devolvido==True):
            print(f"O filme {devolucao.filme} da locação {devolucao.id} foi devolvido ")
        else:
            print(f"O filme {devolucao.filme} da locação {devolucao.id} não foi devolvido")    
    else:
        print(f"locação não encontrada")
 
def devolucao():
      while(True):
        devolver=int (input("Digite o id da locação que você quer devolver: "))
        locacao=Locacao.get_or_none(Locacao.id==devolver)
        if (locacao):
            locacao.devolvido=True
            locacao.save()
            break
        else:
            print(f"locação não encontrada")
            sair=input(f"digite S para sair: ")
            if(sair.upper()=="S"):
                break



###################################   MAIN   ##########################################################



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
    print("[7] - Realizar uma locação")
    print("[8] - Listar todos os clientes")
    print("[9] devolver filme")
    print("[0] - SAIR\n")
    print("......................................\n")
    
    opcao = int(input("Digite a opção desejada:\n"))
    
    if (opcao == 0):
        opcao = False
        break

    elif (opcao == 1):
        cadastrarCliente()

    elif (opcao == 2):
        buscarCliente()
        
    elif (opcao == 3):
        excluirCliente()

    elif (opcao == 4):
        cadastrarFilme()
    
    elif (opcao == 5):
        verificarDevolucao()
    
    elif (opcao == 6):
        verificarFilmesAlugados()
    
    elif (opcao == 7):
        realizarLocacao()

    elif (opcao == 8):
        mostrarTodosClientes()

    elif(opcao==9):
        devolucao()    
    

    input("\nAperte ENTER para continuar (...)")
    