from código.classes_database import *
from código.classe_logica import *

import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()
janela.geometry("650x800")

menubar=tk.Menu(janela)

menu=tk.Menu(menubar,tearoff=False)

menu.add_command(label="Início",command=lambda:frame_inicio.tkraise())
menu.add_command(label="Cliente",command=lambda:frame_cliente.tkraise())
menu.add_command(label="Filme",command=lambda:frame_filme.tkraise())
menu.add_command(label="Locacao",command=lambda:frame_locacao.tkraise())

menu.add_separator()

menu.add_command(label="Sair",command=janela.quit)

menubar.add_cascade(label="Classes",menu=menu)

##########################################################

FONTE = ("Comic Sans MS", 20, "bold")

frame_inicio = tk.Frame(janela, padx=10, pady=10)
frame_filme = tk.Frame(janela, padx=10, pady=10)
frame_cliente = tk.Frame(janela, padx=10, pady=10)
frame_locacao = tk.Frame(janela, padx=10, pady=10)

frame_inicio.grid(row=0,column=0,sticky="nesw")
frame_filme.grid(row=0,column=0,sticky="nesw")
frame_cliente.grid(row=0,column=0,sticky="nesw")
frame_locacao.grid(row=0,column=0,sticky="nesw")

frame_inicio.tkraise()
############################################################


lista_id_cli = []
editando_filme = [False, -1, -1]

def atualizarCliente():
    listbox_cli.delete(0, tk.END)
    lista_id_cli.clear()
    
    for c in Cliente.select():
        listbox_cli.insert(tk.END, c.nome)
        lista_id_cli.append(c.id)
    
    print(f"lista: {lista_id_cli}")

def editarCliente():
    selecao = listbox_cli.curselection()

    if selecao:
        index = selecao[0]
        id = lista_id_cli[index]
        
        editando_filme[0] = True
        editando_filme[1] = id
        editando_filme[2] = index

        texto = listbox_cli.get(index)
        print(f"Indice: {index}, texto: {texto}, id: {id}")

        for c in Cliente.select():
            if c.id == id:
                entry_nome.config(textvariable=(tk.StringVar(value=(c.nome))))
                entry_telefone.config(textvariable=(tk.StringVar(value=(c.telefone))))
                entry_endereco.config(textvariable=(tk.StringVar(value=(c.endereco))))
                print("Achou", texto)

def excluirCliente():
    selecao = listbox_cli.curselection()

    if selecao:
        index = selecao[0]
        id = lista_id_cli[index]
        
        cliente_existe = Cliente.select().where(Cliente.id == id).exists()

        if cliente_existe:
            cliente=Cliente.get_by_id(id)

            cliente.delete_instance()
        
            print(f" o Cliente {cliente.nome} foi excluído.")
            listbox_cli.delete(index)
        else:
            print(f"Não existe nenhum registro equivalente à [ {id} ].")

    atualizarCliente()

def preencherListBox(listbox):  
    for c in Cliente.select():
        print(f"id: {c.id}, nome: {c.nome}")
        listbox_cli.insert(c.id, c.nome)

def cadastrarCliente(nome_cli, telefone_cli, endereco_cli):

    cliente = Cliente.create(nome = nome_cli, telefone = telefone_cli, endereco = endereco_cli)
    
    print(f"Cliente cadastrado com sucesso!")
    print(cliente)
    listbox_cli.insert(cliente.id, nome_cli)

def atualizarDados(nome_cli, telefone_cli, endereco_cli):
    cliente = Cliente.get(Cliente.id == editando_filme[1])

    cliente.nome = nome_cli
    cliente.telefone = telefone_cli
    cliente.endereco = endereco_cli

    cliente.save()

    print(f"Cliente atualizado com sucesso!")
    print(cliente)

    listbox_cli.delete(editando_filme[2])
    listbox_cli.insert(editando_filme[2], nome_cli)


def limparValores():
    entry_nome.config(textvariable=(tk.StringVar(value="")))
    entry_telefone.config(textvariable=(tk.StringVar(value="")))
    entry_endereco.config(textvariable=(tk.StringVar(value="")))

def resgatarValores():
    nome = (entry_nome.get())
    endereco = (entry_endereco.get())
    telefone = (entry_telefone.get())

    if (nome == "") or (endereco == "") or (telefone == ""):
        messagebox.showerror("ERROR_sans", "É necessário inserir os valores para salvar.")
        return

    if (editando_filme[0] == True):
        atualizarDados(nome, telefone, endereco)

        editando_filme[0] = False
        editando_filme[1] = -1
        editando_filme[2] = -1


    else:
        cadastrarCliente(nome, telefone, endereco)
        messagebox.showinfo("3º INFO", f"Deu certo cadastrou o  {nome} .")
    limparValores()
    atualizarCliente()

frame_cliente.columnconfigure


label_titulo = tk.Label(frame_cliente, text="Clientes", font=(FONTE)).grid(column=0, row=0, columnspan=3, padx=200)
label_nome = tk.Label(frame_cliente, text="Nome: ", font=(FONTE)).grid(column=0, row=1)

entry_nome = tk.Entry(frame_cliente, font=(FONTE))
entry_nome.grid(column=1, row=1)

label_telefone = tk.Label(frame_cliente, text="Telefone: ", font=(FONTE)).grid(column=0, row=2)

entry_telefone = tk.Entry(frame_cliente, font=(FONTE))
entry_telefone.grid(column=1, row=2)

label_endereco = tk.Label(frame_cliente, text="Endereço: ", font=(FONTE)).grid(column=0, row=3)

entry_endereco = tk.Entry(frame_cliente, font=(FONTE))
entry_endereco.grid(column=1, row=3)

button_salvar =  tk.Button(frame_cliente, text="salvar", font=(FONTE), command=resgatarValores)
button_salvar.grid(column=0, row=4, pady=30)

button_limpar =  tk.Button(frame_cliente, text="limpar", font=(FONTE), command=limparValores)
button_limpar.grid(column=1, row=4, pady=15)


listbox_cli = tk.Listbox(frame_cliente, width=85, height=25)
listbox_cli.grid(column=0, row=5, columnspan=3, padx=10)


button_editar =  tk.Button(frame_cliente, text="editar", font=(FONTE), command=editarCliente)
button_editar.grid(column=0, row=6, pady=15)

button_excluir =  tk.Button(frame_cliente, text="excluir", font=(FONTE), command=excluirCliente)
button_excluir.grid(column=1, row=6, pady=15)

button_atualizar =  tk.Button(frame_cliente, text="atualizar", font=(FONTE), command=atualizarCliente)
button_atualizar.grid(column=2, row=6, pady=15)

preencherListBox(listbox_cli)

atualizarCliente()

############################################################

lista_id_filme = []
editando_filme = [False, -1, -1]

def atualizarFilme():
    listbox_filme.delete(0, tk.END)
    lista_id_filme.clear()
    
    for c in Filme.select():
        listbox_filme.insert(tk.END, c.titulo)
        lista_id_filme.append(c.id)
    
    print(f"lista: {lista_id_filme}")


def editarFilme():
    selecao = listbox_filme.curselection()

    if selecao:
        index = selecao[0]
        id = lista_id_filme[index]
        
        editando_filme[0] = True
        editando_filme[1] = id
        editando_filme[2] = index

        texto = listbox_filme.get(index)
        print(f"Indice: {index}, texto: {texto}, id: {id}")

        for c in Filme.select():
            if c.id == id:
                entry_diretor.config(textvariable=(tk.StringVar(value=(c.diretor))))
                entry_duracao_minutos.config(textvariable=(tk.StringVar(value=(c.duracao_minutos))))
                entry_titulo.config(textvariable=(tk.StringVar(value=(c.titulo))))
                entry_ano_lancamento.config(textvariable=(tk.StringVar(value=(c.ano_lancamento))))
                print("Achou", texto)


def excluirFilme():
    selecao = listbox_filme.curselection()

    if selecao:
        index = selecao[0]
        id = lista_id_filme[index]
        
        filme_existe = Filme.select().where(Filme.id == id).exists()

        if filme_existe:
            filme=Filme.get_by_id(id)

            filme.delete_instance()
        
            print(f" O filme {filme.titulo} foi excluído.")
            listbox_filme.delete(index)
        else:
            print(f"Não existe nenhum registro equivalente à [ {id} ].")

    atualizarFilme()


def preencherListBox_Filme(listbox_filme):  
    for c in Filme.select():
        print(f"id: {c.id}, nome: {c.titulo}")
        listbox_filme.insert(c.id, c.titulo)


def cadastrarFilme( diretor ,duracao_minutos,  titulo, ano_lancamento):

    filme = Filme.create(diretor=diretor, duracao_minutos=duracao_minutos, titulo=titulo, ano_lancamento=ano_lancamento)
    
    print(f"Filme listado com sucesso!")
    print(filme)
    listbox_filme.insert(filme.id, titulo)


def atualizarDados(diretor ,duracao_minutos,  titulo, ano_lancamento):
    filme = Filme.get(Filme.id == editando_filme[1])

    filme.diretor = diretor
    filme.duracao_minutos = duracao_minutos
    filme.titulo = titulo
    filme.ano_lancamento=ano_lancamento

    filme.save()

    print(f"Filme atualizado com sucesso!")
    print(filme)

    listbox_filme.delete(editando_filme[2])
    listbox_filme.insert(editando_filme[2], titulo)

def limparValores():
    entry_diretor.config(textvariable=(tk.StringVar(value="")))
    entry_duracao_minutos.config(textvariable=(tk.StringVar(value="")))
    entry_titulo.config(textvariable=(tk.StringVar(value="")))  
    entry_ano_lancamento.config(textvariable=(tk.StringVar(value="")))

def resgatarValores():
    diretor = (entry_diretor.get())
    duracao = (entry_duracao_minutos.get())
    titulo = (entry_titulo.get())
    ano=(entry_ano_lancamento.get())

    if (diretor == "") or (duracao == "") or (titulo == "") or (ano==""):
        messagebox.showerror("ERROR_sans", "É necessário inserir os valores para salvar.")
        return

    if (editando_filme[0] == True):
        atualizarDados(diretor, duracao, titulo , ano)

        editando_filme[0] = False
        editando_filme[1] = -1,
        editando_filme[2] = -1


    else:
        cadastrarFilme(diretor, duracao , titulo, ano)
        messagebox.showinfo("3º INFO", f"Deu certo cadastrou o  {titulo} .")
    limparValores()
    atualizarFilme()

frame_filme.columnconfigure

# Título
label_titulo = tk.Label(frame_filme, text="Filmes", font=FONTE)
label_titulo.grid(column=0, row=0, columnspan=2, pady=20)

# Linha 1 - Título
label_titulo_filme = tk.Label(frame_filme, text="Título: ", font=FONTE)
label_titulo_filme.grid(column=0, row=1, sticky="e", padx=10, pady=5)
entry_titulo = tk.Entry(frame_filme, font=FONTE)
entry_titulo.grid(column=1, row=1, sticky="w", padx=10, pady=5)

# Linha 2 - Diretor
label_diretor = tk.Label(frame_filme, text="Diretor: ", font=FONTE)
label_diretor.grid(column=0, row=2, sticky="e", padx=10, pady=5)
entry_diretor = tk.Entry(frame_filme, font=FONTE)
entry_diretor.grid(column=1, row=2, sticky="w", padx=10, pady=5)

# Linha 3 - Duração
label_duracao = tk.Label(frame_filme, text="Duração (min): ", font=FONTE)
label_duracao.grid(column=0, row=3, sticky="e", padx=10, pady=5)
entry_duracao_minutos = tk.Entry(frame_filme, font=FONTE)
entry_duracao_minutos.grid(column=1, row=3, sticky="w", padx=10, pady=5)

# Linha 4 - Ano de Lançamento
label_ano = tk.Label(frame_filme, text="Ano de Lançamento: ", font=FONTE)
label_ano.grid(column=0, row=4, sticky="e", padx=10, pady=5)
entry_ano_lancamento = tk.Entry(frame_filme, font=FONTE)
entry_ano_lancamento.grid(column=1, row=4, sticky="w", padx=10, pady=5)

# Linha 5 - Botões
button_salvar = tk.Button(frame_filme, text="Salvar", font=FONTE, command=resgatarValores)
button_salvar.grid(column=0, row=5, pady=20, padx=10, sticky="e")

button_limpar = tk.Button(frame_filme, text="Limpar", font=FONTE, command=limparValores)
button_limpar.grid(column=1, row=5, pady=20, padx=10, sticky="w")

button_editar = tk.Button(frame_filme, text="Editar", font=FONTE, command=editarFilme)
button_editar.grid(column=0, row=6, pady=10, padx=10, sticky="e")

button_atualizar = tk.Button(frame_filme, text="Atualizar", font=FONTE, command=atualizarFilme)
button_atualizar.grid(column=1, row=6, pady=10, padx=10, sticky="w")

button_excluir =  tk.Button(frame_filme, text="excluir", font=(FONTE), command=excluirFilme)
button_excluir.grid(column=1, row=6,padx=200, pady=15)

# Linha 7 - Listbox
listbox_filme = tk.Listbox(frame_filme, width=85, height=25)
listbox_filme.grid(column=0, row=7, columnspan=2, padx=10, pady=20)

preencherListBox_Filme(listbox_filme)

janela.config(menu=menubar)
janela.mainloop()