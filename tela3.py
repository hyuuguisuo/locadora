from código.classes_database import *
from código.classe_logica import *

import tkinter as tk
from tkinter import messagebox

lista_id = []
editando = [False, -1, -1]
    
def resetarEditando():
    editando[0] = False
    editando[1] = -1
    editando[2] = -1

def resgatarValores():
    global editando

    cliente = (entry_cliente.get())
    filme = (entry_filme.get())
    valor = (entry_valor.get())

    if (cliente == "") or (filme == "") or (valor == ""):
        messagebox.showerror("ERROR_sans", "É necessário inserir os valores para salvar.")
        return
    if (editando[0] == True):
        # alterarLocacao(nome, telefone, endereco)
        resetarEditando()
    else:
        cadastrarLocacao(cliente, filme, valor)
        messagebox.showinfo("3º INFO", f"Deu certo cadastrou a locacao: {cliente} | Filme: {filme} .")
    limparValores()
    
def cadastrarLocacao(nome_cli, nome_filme, valor_locacao):

    locacao = Locacao.create(cliente = nome_cli, filme = nome_filme, valor = valor_locacao)
    
    print(f"Locação cadastrado com sucesso!")
    print(locacao)
    
    listbox.insert(locacao.id, (f"[{locacao.id}] Cliente: {locacao.cliente.nome} | Filme: {locacao.filme.titulo}"))

def limparValores():
    entry_cliente.config(textvariable=(tk.StringVar(value="")))
    entry_filme.config(textvariable=(tk.StringVar(value="")))
    entry_valor.config(textvariable=(tk.StringVar(value="")))

    resetarEditando()

def editarLocacao():
    pass

def excluirLocacao():
    pass

def atualizarLocacao():
    listbox.delete(0, tk.END)
    lista_id.clear()
    
    for l in Locacao.select():
        listbox.insert(l.id, (f"[{l.id}] Cliente: {l.cliente.nome} | Filme: {l.filme.titulo}"))
        lista_id.append(l.id)
    
    print(f"lista: {lista_id}")
    
    print("editando: ", editando[0], "id: ", editando[1], "index: ", editando[2])

    resetarEditando()


def preencherListBox(listbox):
    for l in Locacao.select():
        print(f"id: [{l.id}] Cliente: {l.cliente.nome} | Filme: {l.filme.titulo}")
        listbox.insert(l.id, (f"[{l.id}] Cliente: {l.cliente.nome} | Filme: {l.filme.titulo}"))


janela = tk.Tk()
janela.geometry("650x800")

FONTE = ("Comic Sans MS", 20, "bold")

janela.columnconfigure
label_titulo = tk.Label(janela, text="* Cadastro de Locação *", font=(FONTE)).grid(column=0, row=0, columnspan=3, padx=150)


label_cliente = tk.Label(janela, text="Cliente: ", font=(FONTE)).grid(column=0, row=1)
entry_cliente = tk.Entry(janela, font=(FONTE))
entry_cliente.grid(column=1, row=1)


label_filme = tk.Label(janela, text="Filme: ", font=(FONTE)).grid(column=0, row=2)
entry_filme = tk.Entry(janela, font=(FONTE))
entry_filme.grid(column=1, row=2)


label_valor = tk.Label(janela, text="Valor: ", font=(FONTE)).grid(column=0, row=3)
entry_valor = tk.Entry(janela, font=(FONTE))
entry_valor.grid(column=1, row=3)

label_devolvido = tk.Label(janela, text="Devolvido: Sim", font=(("Comic Sans MS", 14, "bold"))).grid(column=0, row=4)
label_dt_locacao = tk.Label(janela, text="Data da locação: \nDD/MM/AA", font=(("Comic Sans MS", 14, "bold"))).grid(column=1, row=4)
label_dt_devolucao = tk.Label(janela, text="Limite de devolução: \nDD/MM/AA", font=(("Comic Sans MS", 14, "bold"))).grid(column=2, row=4)

button_salvar =  tk.Button(janela, text="salvar", font=(FONTE), command=resgatarValores)
button_salvar.grid(column=0, row=5, pady=30)

button_limpar =  tk.Button(janela, text="limpar", font=(FONTE), command=limparValores)
button_limpar.grid(column=1, row=5, pady=15)


listbox = tk.Listbox(janela, width=85, height=20)
listbox.grid(column=0, row=6, columnspan=3, padx=10)


button_editar =  tk.Button(janela, text="editar", font=(FONTE), command=editarLocacao)
button_editar.grid(column=0, row=7, pady=13)

button_excluir =  tk.Button(janela, text="excluir", font=(FONTE), command=excluirLocacao)
button_excluir.grid(column=1, row=7, pady=13)

button_atualizar =  tk.Button(janela, text="atualizar", font=(FONTE), command=atualizarLocacao)
button_atualizar.grid(column=2, row=7, pady=13)


preencherListBox(listbox)
atualizarLocacao()


janela.mainloop()
