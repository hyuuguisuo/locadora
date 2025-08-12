from código.classes_database import *
from código.classe_logica import *

import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()
janela.geometry("550x800")

FONTE = ("Comic Sans MS", 20, "bold")

def preencherDados(event):
    selecao = listbox.curselection()

    if selecao:
        indice = selecao[0]
        texto = listbox.get(indice)
        # print(f"Selecionou: {texto}")
        
        for c in Cliente.select():
            if c.nome == texto:
                entry_nome.config(textvariable=(tk.StringVar(value=(c.nome))))
                entry_telefone.config(textvariable=(tk.StringVar(value=(c.telefone))))
                entry_endereco.config(textvariable=(tk.StringVar(value=(c.endereco))))
                print("Achou", texto)




def cadastrarCliente(nome_cli, telefone_cli, endereco_cli):

    cliente = Cliente.create(nome = nome_cli, telefone = telefone_cli, endereco = endereco_cli)
    
    print(f"Cliente cadastrado com sucesso!")
    print(cliente)

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

    cadastrarCliente(nome, telefone, endereco)
    listbox.insert(tk.END, nome)
    limparValores()


label_titulo = tk.Label(janela, text="Clientes", font=(FONTE)).grid(column=0, row=0, columnspan=2, padx=200)


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
listbox.grid(column=0, row=5, columnspan=2, padx=10)

listbox.bind("<<ListboxSelect>>", preencherDados)

janela.mainloop()