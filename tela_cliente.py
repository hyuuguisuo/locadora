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

frame_cliente.tkraise()
############################################################

def listarClientes():
    listbox_cli.delete(0, tk.END)
    for cliente in Cliente.select():
        print(f"id: {cliente.id}, nome: {cliente.nome}")
        listbox_cli.insert(cliente.id, f"{cliente.id} : : {cliente.nome}")

def cadastrarCliente():
    global editando_cli

    nome = (entry_nome.get())
    endereco = (entry_endereco.get())
    telefone = (entry_telefone.get())

    if not nome or not endereco or not telefone:
        messagebox.showerror("ERROR_sans", "É necessário inserir os valores para salvar.")
        return
    
    try:
        Cliente.create(nome = nome, telefone = telefone, endereco = endereco) 
        messagebox.showinfo("3º INFO", f"Deu certo cadastrou o  {nome} .")
        listarClientes()
        entry_nome.delete(0, tk.END)
        entry_endereco.delete(0, tk.END)
        entry_telefone.delete(0, tk.END)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao cadastrar: {e}")

def excluirCliente():
    selecionado = listbox_cli.curselection()
    if not selecionado:
        messagebox.showwarning("Atenção", "Selecione um cliente para excluir.")
        return
    

    cliente_selecionado = listbox_cli.get(selecionado[0])
    cliente_id = int(cliente_selecionado.split(" : : ")[0])
    try:
        cliente = Cliente.get_by_id(cliente_id)
        messagebox.showinfo("é", f"O(A) Cliente '{cliente.nome}' foi excluído(a)!")
        cliente.delete_instance()
        listarClientes()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao excluir....: {e}")

def editarCliente():
    global editando_cli

    print(f"estou editando: {editando_cli}")
    if (editando_cli != None):
        try:
            cliente = Cliente.get_by_id(editando_cli)
            novo_nome = (entry_nome.get())
            novo_endereco = (entry_endereco.get())
            novo_telefone = (entry_telefone.get())
            if not novo_nome or not novo_endereco or not novo_telefone:
                messagebox.showwarning("Atenção", "tem que colocar as coisas")
                return
            
            cliente.nome = novo_nome
            cliente.endereco = novo_endereco
            cliente.telefone = novo_telefone

            cliente.save()
            messagebox.showinfo("Sucesso", "O cliente foi editado!")
            
            listarClientes()
            editando_cli = None

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao editar o cliente: {e}")
    else:
         messagebox.showerror("Erro", f"Selecione um cliente para editar: {e}")

def preencherListbox_Cliente(event):
    global editando_cli
    
    selecionado = listbox_cli.curselection()
    if not selecionado:
        return
    
    cliente_selecionado = listbox_cli.get(selecionado[0])

    if cliente_selecionado:
        cliente_id = int(cliente_selecionado.split(' : : ')[0])
        cliente = Cliente.get_by_id(cliente_id)

        if (cliente):    
            editando_cli = cliente_id
            entry_nome.config(textvariable=(tk.StringVar(value=(cliente.nome))))
            entry_telefone.config(textvariable=(tk.StringVar(value=(cliente.telefone))))
            entry_endereco.config(textvariable=(tk.StringVar(value=(cliente.endereco))))
            print(f"estou editando: {editando_cli}")
            
editando_cli = None

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

button_cadastrar =  tk.Button(frame_cliente, text="Cadastrar", font=(FONTE), command=cadastrarCliente)
button_cadastrar.grid(column=0, row=4, pady=30)

button_editar =  tk.Button(frame_cliente, text="Editar", font=(FONTE), command=editarCliente)
button_editar.grid(column=0, row=6, pady=15)

button_excluir =  tk.Button(frame_cliente, text="Excluir", font=(FONTE), command=excluirCliente)
button_excluir.grid(column=1, row=6, pady=15)

button_atualizar =  tk.Button(frame_cliente, text="Atualizar", font=(FONTE), command=listarClientes)
button_atualizar.grid(column=2, row=6, pady=15)

listbox_cli = tk.Listbox(frame_cliente, width=85, height=25)
listbox_cli.grid(column=0, row=5, columnspan=3, padx=10)

listbox_cli.bind('<<ListboxSelect>>', preencherListbox_Cliente)

listarClientes()

######################################################################################







janela.config(menu=menubar)
janela.mainloop()