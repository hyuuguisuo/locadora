from código.classes_database import *
from código.classe_logica import *

import tkinter as tk
from tkinter import messagebox

lista_id = []
editando = [False, -1, -1]

def atualizarCliente():
    listbox.delete(0, tk.END)
    lista_id.clear()
    
    for c in Cliente.select():
        listbox.insert(tk.END, c.nome)
        lista_id.append(c.id)
    
    print(f"lista: {lista_id}")

def editarCliente():
    selecao = listbox.curselection()

    if selecao:
        index = selecao[0]
        id = lista_id[index]
        
        editando[0] = True
        editando[1] = id
        editando[2] = index

        texto = listbox.get(index)
        print(f"Indice: {index}, texto: {texto}, id: {id}")

        for c in Cliente.select():
            if c.id == id:
                entry_nome.config(textvariable=(tk.StringVar(value=(c.nome))))
                entry_telefone.config(textvariable=(tk.StringVar(value=(c.telefone))))
                entry_endereco.config(textvariable=(tk.StringVar(value=(c.endereco))))
                print("Achou", texto)

def excluirCliente():
    selecao = listbox.curselection()

    if selecao:
        index = selecao[0]
        id = lista_id[index]
        
        cliente_existe = Cliente.select().where(Cliente.id == id).exists()

        if cliente_existe:
            cliente=Cliente.get_by_id(id)

            cliente.delete_instance()
        
            print(f" o Cliente {cliente.nome} foi excluído.")
            listbox.delete(index)
        else:
            print(f"Não existe nenhum registro equivalente à [ {id} ].")

    atualizarCliente()

def preencherListBox(listbox):  
    for c in Cliente.select():
        print(f"id: {c.id}, nome: {c.nome}")
        listbox.insert(c.id, c.nome)
                

def cadastrarCliente(nome_cli, telefone_cli, endereco_cli):

    cliente = Cliente.create(nome = nome_cli, telefone = telefone_cli, endereco = endereco_cli)
    
    print(f"Cliente cadastrado com sucesso!")
    print(cliente)
    listbox.insert(cliente.id, nome_cli)

def atualizarDados(nome_cli, telefone_cli, endereco_cli):
    cliente = Cliente.get(Cliente.id == editando[1])

    cliente.nome = nome_cli
    cliente.telefone = telefone_cli
    cliente.endereco = endereco_cli

    cliente.save()

    print(f"Cliente atualizado com sucesso!")
    print(cliente)

    listbox.delete(editando[2])
    listbox.insert(editando[2], nome_cli)


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

    if (editando[0] == True):
        atualizarDados(nome, telefone, endereco)

        editando[0] = False
        editando[1] = -1
        editando[2] = -1


    else:
        cadastrarCliente(nome, telefone, endereco)
        messagebox.showinfo("3º INFO", f"Deu certo cadastrou o  {nome} .")
    limparValores()
    atualizarCliente()

# tela # 
janela = tk.Tk()
janela.geometry("650x800")

FONTE = ("Comic Sans MS", 20, "bold")

janela.columnconfigure


label_titulo = tk.Label(janela, text="Clientes", font=(FONTE)).grid(column=0, row=0, columnspan=3, padx=200)
label_nome = tk.Label(janela, text="Nome: ", font=(FONTE)).grid(column=0, row=1)

entry_nome = tk.Entry(janela, font=(FONTE))
entry_nome.grid(column=1, row=1)

label_telefone = tk.Label(janela, text="Telefone: ", font=(FONTE)).grid(column=0, row=2)

entry_telefone = tk.Entry(janela, font=(FONTE))
entry_telefone.grid(column=1, row=2)

label_endereco = tk.Label(janela, text="Endereço: ", font=(FONTE)).grid(column=0, row=3)

entry_endereco = tk.Entry(janela, font=(FONTE))
entry_endereco.grid(column=1, row=3)



button_salvar =  tk.Button(janela, text="salvar", font=(FONTE), command=resgatarValores)
button_salvar.grid(column=0, row=4, pady=30)

button_limpar =  tk.Button(janela, text="limpar", font=(FONTE), command=limparValores)
button_limpar.grid(column=1, row=4, pady=15)


listbox = tk.Listbox(janela, width=85, height=25)
listbox.grid(column=0, row=5, columnspan=3, padx=10)


button_editar =  tk.Button(janela, text="editar", font=(FONTE), command=editarCliente)
button_editar.grid(column=0, row=6, pady=15)

button_excluir =  tk.Button(janela, text="excluir", font=(FONTE), command=excluirCliente)
button_excluir.grid(column=1, row=6, pady=15)

button_atualizar =  tk.Button(janela, text="atualizar", font=(FONTE), command=atualizarCliente)
button_atualizar.grid(column=2, row=6, pady=15)

preencherListBox(listbox)

atualizarCliente()

janela.mainloop()