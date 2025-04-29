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
        nome_cli = input("Digite o nome do cliente:\n -> ")

        for c in Cliente.select().where(Cliente.nome == nome_cli):
            print(f" -> | {c.nome}")
        
    elif (opcao == 3):
        nome_cli = input("Digite o nome do cliente:\n -> ")
        cliente = Cliente.delete().where(Cliente.nome == nome_cli)
        print("s")

    elif (opcao == 4):
        print("----------------------------------")
        titulo_filme= input("Digite o título do filme:\n -> ")
        ano_lancamento_filme= input("Digite o ano de lançamento do filme:\n -> ")
        diretor_filme = input("O nome do diretor:\n -> ")
        duracao_minutos_filme = input("...e a duração total do filme (minutos):\n -> ")

        filme = Filme.create(titulo = titulo_filme, ano_lancamento = ano_lancamento_filme, diretor = diretor_filme, duracao_minutos = duracao_minutos_filme)

    input("\nAperte ENTER para continuar (...)")