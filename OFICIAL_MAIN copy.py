from código.classes_database import *
from código.classe_logica import *

import tkinter as tk
from tkinter import messagebox, ttk

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


def listarFilmes():
    listbox_filme.delete(0, tk.END)
    for filme in Filme.select():
        print(f"id: {filme.id}, nome: {filme.titulo}")
        listbox_filme.insert(filme.id, f"{filme.id} : : {filme.titulo}")

def cadastrarFilme():
    global editando_filme

    titulo = (entry_titulo.get())
    diretor = (entry_diretor.get())
    duracao = (entry_duracao_minutos.get())
    ano = (entry_ano_lancamento.get())

    if not titulo or not diretor or not duracao or not ano:
        messagebox.showerror("ERROR_sans", "É necessário inserir os valores para salvar.")
        return
    
    try:
        Filme.create(titulo = titulo, diretor = diretor, duracao = duracao, ano = ano) 
        messagebox.showinfo("3º INFO", f"Deu certo cadastrou o filme  {titulo} .")
        listarFilmes()
        entry_titulo.delete(0, tk.END)
        entry_diretor.delete(0, tk.END)
        entry_duracao_minutos.delete(0, tk.END)
        entry_ano_lancamento.delete(0, tk.END)

    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao cadastrar o filme: {e}")

def excluirFilme():
    selecionado = listbox_filme.curselection()
    if not selecionado:
        messagebox.showwarning("Atenção", "Selecione um filme para excluir.")
        return
    

    filme_selecionado = listbox_filme.get(selecionado[0])
    filme_id = filme_selecionado.split(" : : ")[0]
    try:
        filme = Filme.get_by_id(filme_id)
        messagebox.showinfo("é", f"O Filme '{filme.titulo}' foi excluído!")
        filme.delete_instance()
        listarFilmes()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao excluir....: {e}")

def editarFilme():
    global editando_filme

    if (editando_filme != None):
        try:
            filme = Filme.get_by_id(editando_filme)
            novo_titulo = (entry_titulo.get())
            novo_diretor = (entry_diretor.get())
            nova_duracao = (entry_duracao_minutos.get())
            novo_ano = (entry_ano_lancamento.get())

            if not novo_titulo or not novo_diretor or not nova_duracao or not ano:
                messagebox.showerror("ERROR_sans", "É necessário inserir os valores para salvar.")
                return
        
            filme.titulo = novo_titulo
            filme.diretor = novo_diretor
            filme.duracao = nova_duracao
            filme.ano_lancamento = novo_ano
            filme.save()
            messagebox.showinfo("Sucesso", "O filme foi editado!@")
            
            listarFilmes()
            editando_filme = None

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao editar o filme >: {e}")
    else:
         messagebox.showerror("Erro", f"Selecione um filme para editar: {e}")

def preencherlistbox_filme(event):
    global editando_filme
    
    selecionado = listbox_filme.curselection()
    if not selecionado:
        return
    
    filme_selecionado = listbox_filme.get(selecionado[0])

    if filme_selecionado:
        filme_id = int(filme_selecionado.split(' : : ')[0])
        filme = Filme.get_by_id(filme_id)

        if (filme):    
            editando_filme = filme_id
            entry_titulo.config(textvariable=(tk.StringVar(value=(filme.titulo))))
            entry_diretor.config(textvariable=(tk.StringVar(value=(filme.diretor))))
            entry_duracao_minutos.config(textvariable=(tk.StringVar(value=(filme.duracao_minutos))))
            entry_ano_lancamento.config(textvariable=(tk.StringVar(value=(filme.ano_lancamento))))
            print(f"estou editando: {editando_filme}")
            
editando_filme = None

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

button_cadastrar =  tk.Button(frame_filme, text="Cadastrar", font=(FONTE), command=cadastrarFilme)
button_cadastrar.grid(column=0, row=4, pady=30)

button_editar =  tk.Button(frame_filme, text="Editar", font=(FONTE), command=editarFilme)
button_editar.grid(column=0, row=6, pady=15)

button_excluir =  tk.Button(frame_filme, text="Excluir", font=(FONTE), command=excluirFilme)
button_excluir.grid(column=1, row=6, pady=15)

button_atualizar =  tk.Button(frame_filme, text="Atualizar", font=(FONTE), command=listarFilmes)
button_atualizar.grid(column=2, row=6, pady=15)

listbox_filme = tk.Listbox(frame_filme, width=85, height=25)
listbox_filme.grid(column=0, row=5, columnspan=3, padx=10)

listbox_filme.bind('<<ListboxSelect>>', preencherlistbox_filme)

listarFilmes()

######################################################################################

def salvarLocacao():
    try:
        cliente_selecionado = combobox_cliente.get()
        cliente_id = int(cliente_selecionado.split(" : : ")[0])
        cliente = Cliente.get_by_id(cliente_id)

        filmes_selecionado = combobox_filme.get() 
        filme_id = int(filmes_selecionado.split(" : : ")[0])
        filme = Cliente.get_by_id(filme_id)

        dt_locacao_2 = date.today()
    
        dias_locacao = 14

        dt_devolucao_2 = dt_locacao_2 + timedelta(days=dias_locacao)

        if (cliente and filme):
            nova_locacao = Locacao.create(
                cliente=cliente_id,
                filme=filme_id,
                dt_locacao = dt_locacao_2,
                dt_devolucao = dt_devolucao_2,
                valor = 20,
                devolvido=False
            )
            messagebox.showinfo("Sucesso", f"Locacao entre '{nova_locacao.cliente.nome}' e '{nova_locacao.filme.titulo}' salva com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao salvar a locação: {e}")

# Criar um label para cliente
label_cliente = tk.Label(frame_locacao, text="Cliente:")
label_cliente.grid(row=0, column=0, padx=10, pady=10, sticky="e")

clientes = [f"{cli.id} : : {cli.nome}" for cli in Cliente.select()]

combobox_cliente = ttk.Combobox(frame_locacao, values=clientes)
combobox_cliente.grid(row=0, column=1, padx=10, pady=10, sticky="we")


filmes = [f"{filme.id} : : {filme.titulo}" for filme in Filme.select()]

combobox_filme = ttk.Combobox(frame_locacao, values=filmes)
combobox_filme.grid(row=1, column=1, padx=10, pady=10, sticky="we")


# Botões para "salvar"
button_salvar = tk.Button(frame_locacao, text="Salvar", command=salvarLocacao)
button_salvar.grid(row=3, column=0, pady=20)




##mensagem inicial

l_mens = tk.Label(frame_inicio,text="Seja bem vindo ao nosso sistema", font=("Arial", 20),  )
l_mens.grid(row=0,column=0, sticky="ew", columnspan=4)
l_mens2 = tk.Label(frame_inicio,text="Equipe: Guilherme Oreste e Guilherme Henrique", font=("Arial", 20),  )
l_mens2.grid(row=1,column=0,pady= 20 ,  sticky="ew", columnspan=4)
l_mens3 = tk.Label(frame_inicio,text="(👉ﾟヮﾟ)👉", font=("Arial", 20),  )
l_mens3.grid(row=2,column=0,pady= 20 ,  sticky="ew", columnspan=4)

janela.config(menu=menubar)
janela.mainloop()


