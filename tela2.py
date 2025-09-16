from código.classes_database import *
from código.classe_logica import *

import tkinter as tk
from tkinter import messagebox

lista_id = []
editando = [False, -1, -1]

def atualizarFilme():
    listbox.delete(0, tk.END)
    lista_id.clear()
    
    for c in Filme.select():
        listbox.insert(tk.END, c.nome)
        lista_id.append(c.id)
    
    print(f"lista: {lista_id}")


def editarFilme():
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
                entry_diretor.config(textvariable=(tk.StringVar(value=(c.diretor))))
                entry_duracao_minutos.config(textvariable=(tk.StringVar(value=(c.duracao_minutos))))
                entry_titulo.config(textvariable=(tk.StringVar(value=(c.titulo))))
                entry_ano_lancamento.config(textvariable=(tk.StringVar(value=(c.ano_lancamento))))
                print("Achou", texto)


def preencherListBox(listbox):  
    for c in Filme.select():
        print(f"id: {c.id}, nome: {c.titulo}")
        listbox.insert(c.id, c.titulo)


def cadastrarFilme( diretor ,duracao_minutos,  titulo, ano_lancamento):

    filme = Filme.create(diretor=diretor, duracao_minutos=duracao_minutos, titulo=titulo, ano_lancamento=ano_lancamento)
    
    print(f"Filme listado com sucesso!")
    print(filme)
    listbox.insert(filme.id, titulo)


def atualizarDados(diretor ,duracao_minutos,  titulo, ano_lancamento):
    filme = Filme.get(Filme.id == editando[1])

    filme.diretor = diretor
    filme.duracao_minutos = duracao_minutos
    filme.titulo = titulo
    filme.ano_lancamento=ano_lancamento

    filme.save()

    print(f"Filme atualizado com sucesso!")
    print(filme)

    listbox.delete(editando[2])
    listbox.insert(editando[2], titulo)

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

    if (editando[0] == True):
        atualizarDados(diretor, duracao, titulo , ano)

        editando[0] = False
        editando[1] = -1
        editando[2] = -1


    else:
        cadastrarFilme(diretor, duracao , titulo, ano)
        messagebox.showinfo("3º INFO", f"Deu certo cadastrou o  {titulo} .")
    limparValores()
    atualizarFilme()


# tela # 
janela = tk.Tk()
janela.geometry("800x800")

FONTE = ("Comic Sans MS", 20, "bold")

janela.columnconfigure

# Título
label_titulo = tk.Label(janela, text="Filmes", font=FONTE)
label_titulo.grid(column=0, row=0, columnspan=2, pady=20)

# Linha 1 - Título
label_titulo_filme = tk.Label(janela, text="Título: ", font=FONTE)
label_titulo_filme.grid(column=0, row=1, sticky="e", padx=10, pady=5)
entry_titulo = tk.Entry(janela, font=FONTE)
entry_titulo.grid(column=1, row=1, sticky="w", padx=10, pady=5)

# Linha 2 - Diretor
label_diretor = tk.Label(janela, text="Diretor: ", font=FONTE)
label_diretor.grid(column=0, row=2, sticky="e", padx=10, pady=5)
entry_diretor = tk.Entry(janela, font=FONTE)
entry_diretor.grid(column=1, row=2, sticky="w", padx=10, pady=5)

# Linha 3 - Duração
label_duracao = tk.Label(janela, text="Duração (min): ", font=FONTE)
label_duracao.grid(column=0, row=3, sticky="e", padx=10, pady=5)
entry_duracao_minutos = tk.Entry(janela, font=FONTE)
entry_duracao_minutos.grid(column=1, row=3, sticky="w", padx=10, pady=5)

# Linha 4 - Ano de Lançamento
label_ano = tk.Label(janela, text="Ano de Lançamento: ", font=FONTE)
label_ano.grid(column=0, row=4, sticky="e", padx=10, pady=5)
entry_ano_lancamento = tk.Entry(janela, font=FONTE)
entry_ano_lancamento.grid(column=1, row=4, sticky="w", padx=10, pady=5)

# Linha 5 - Botões
button_salvar = tk.Button(janela, text="Salvar", font=FONTE, command=resgatarValores)
button_salvar.grid(column=0, row=5, pady=20, padx=10, sticky="e")

button_limpar = tk.Button(janela, text="Limpar", font=FONTE, command=limparValores)
button_limpar.grid(column=1, row=5, pady=20, padx=10, sticky="w")

button_editar = tk.Button(janela, text="Editar", font=FONTE, command=editarFilme)
button_editar.grid(column=0, row=6, pady=10, padx=10, sticky="e")

button_atualizar = tk.Button(janela, text="Atualizar", font=FONTE, command=atualizarFilme)
button_atualizar.grid(column=1, row=6, pady=10, padx=10, sticky="w")

# Linha 7 - Listbox
listbox = tk.Listbox(janela, width=85, height=25)
listbox.grid(column=0, row=7, columnspan=2, padx=10, pady=20)

atualizarFilme()
janela.mainloop()




  
