from datetime import date, timedelta
from classes import *

def verificarQuantidadeFilmes():
    print("===================|| QUANTIDADE DE FILMES ALUGADOS ||===================\n")
    for c in Locacao.select():
        filme = Filme.get(Filme.id == c.filme)
        print(f" -> | {filme.titulo}")

def realizarLocacao():
    id_cli = int(input("DIGITE O ID DO CLIENTE QUE IRÁ REALIZAR A LOCAÇÃO:\n"))
    id_filme = int(input("DIGITE O ID DO FILME QUE SERÁ LOCADO\n"))
    
    valor_2 = float(input("DIGITE O VALOR DO FILME:\n"))
    
    dt_locacao_2 = date.today()
    
    dias_locacao = 14

    dt_devolucao_2 = dt_locacao_2 + timedelta(days=dias_locacao)

    locacao = Locacao.create(cliente = id_cli, filme = id_filme, dt_locacao = dt_locacao_2, dt_devolucao = dt_devolucao_2, valor = valor_2)

def mostrarTodosClientes():
    for c in Cliente.select():
        print(f" -> | {c.nome}")