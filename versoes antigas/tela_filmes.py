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


janela.config(menu=menubar)
janela.mainloop()