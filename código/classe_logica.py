from datetime import date, timedelta
from código.classes_database import *

def verificarFilmesAlugados():
    print("---- QUANTIDADE DE FILMES ALOCADOS ----\n")
    
    locacoes = (Locacao.select(Locacao, Filme).join(Filme, JOIN.LEFT_OUTER))
    encontrou = False

    for c in locacoes:
        encontrou = True
        if c.filme:
            print(f" -> | ID: [{c.filme.id}]  |  {c.filme}")
        else:
            print(f"[AVISO] Locação ID {c.id} com filme ID {c.filme_id} não existe.")

    if not encontrou:
        print("Nenhuma locação encontrada.")

        

def realizarLocacao():
    print("---------- REALIZAR LOCAÇÃO ----------\n")

    id_cli = int(input("DIGITE O ID DO CLIENTE QUE IRÁ REALIZAR A LOCAÇÃO:\n"))
    id_filme = int(input("DIGITE O ID DO FILME QUE SERÁ LOCADO\n"))
    
    valor_2 = float(input("DIGITE O VALOR DO FILME (R$):\n"))
    
    dt_locacao_2 = date.today()
    
    dias_locacao = 14

    dt_devolucao_2 = dt_locacao_2 + timedelta(days=dias_locacao)



    ###
    existeCli = False
    existeFil = False


    for c in Cliente.select():
        if (c.id == id_cli):
            existeCli = True

    for c in Filme.select():
        if (c.id == id_filme):
            existeFil = True

    if (existeFil == True and existeCli == True):
        locacao = Locacao.create(cliente = id_cli, filme = id_filme, dt_locacao = dt_locacao_2, dt_devolucao = dt_devolucao_2, valor = valor_2, devolvido = False)
        print("A locação foi realizada com sucesso!")
        print(locacao)
    
    if (existeCli == False):
        print("Este ID do cliente não existe.")

    if (existeFil == False):
        print("Este ID do filme não existe.")

def mostrarTodosClientes():
    print("---------- MOSTRAR CLIENTES ---------\n")

    for c in Cliente.select():
        print(f" -> | ID: [{c.id}]  |  {c.nome}")