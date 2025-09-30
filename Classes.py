from datetime import date, timedelta
import sys
import os
from código.classes_database import Cliente, Filme, Locacao

import tkinter as tk
from tkinter import messagebox, ttk

class Locadora():
    def __init__(self):
            self.FONT_TITULO = ("Comic Sans MS", 18)
            self.FONT_TEXTO = ("Comic Sans MS", 13)

            self.editando_cli= None
            self.editando_filme = None
  
            self.criar_janela_principal()
            self.criar_menu()
            self.criar_frames()
            self.iniciar_aplicacao()

    def criar_janela_principal(self):
        self.janela = tk.Tk()
        self.janela.title("Locadora de Filmes para alocar na locadora de filmes.")
        self.janela.geometry("650x800")
    
    def criar_menu(self):
        self.menubar = tk.Menu(self.janela)
        
        menu_classes = tk.Menu(self.menubar, tearoff=False)

        menu_classes.add_command(label="Início", command=self.mostrar_inicio)
        menu_classes.add_command(label="Cliente", command=self.mostrar_cliente)
        menu_classes.add_command(label="Filme", command=self.mostrar_filme)
        menu_classes.add_command(label="Locacao", command=self.mostrar_locacao)
        
        menu_classes.add_separator()

        menu_classes.add_command(label="Sair", command=self.janela.quit)

        self.menubar.add_cascade(label="Classes", menu=menu_classes)

        menu_sobre = tk.Menu(self.menubar, tearoff=False)

        menu_sobre.add_command(label="Sobre Nós", command=self.mostrar_sobre)
        
        menu_sobre.add_separator()
        
        menu_sobre.add_command(label="Versão", command=lambda: messagebox.showinfo("Versão Atual", "Versão 1.0"))
        
        self.menubar.add_cascade(label="Sobre", menu=menu_sobre)
    
    def criar_frames(self):
        self.criar_frame_inicio()
        self.criar_frame_filme()
        self.criar_frame_cliente()
        self.criar_frame_locacao()

        self.frame_inicio.grid(row=0,column=0,sticky="nesw")
        self.frame_filme.grid(row=0,column=0,sticky="nesw")
        self.frame_cliente.grid(row=0,column=0,sticky="nesw")
        self.frame_locacao.grid(row=0,column=0,sticky="nesw")
    
    def criar_frame_inicio(self):
        self.frame_inicio = tk.Frame(self.janela)
        
        l_mens = tk.Label(self.frame_inicio,text="Seja bem vindo ao nosso sistema", font=("Arial", 20),  )
        l_mens.grid(row=0,column=0, sticky="ew", columnspan=4)
        l_mens2 = tk.Label(self.frame_inicio,text="Equipe: Guilherme Oreste e Guilherme Henrique", font=("Arial", 20),  )
        l_mens2.grid(row=1,column=0,pady= 20 ,  sticky="ew", columnspan=4)
        l_mens3 = tk.Label(self.frame_inicio,text="(👉ﾟヮﾟ)👉", font=("Arial", 20),  )
        l_mens3.grid(row=2,column=0,pady= 20 ,  sticky="ew", columnspan=4)
    
    def criar_frame_sobre(self):
        self.frame_sobre = tk.Frame(self.janela)
        lb_alunos = tk.Label(self.frame_sobre, text="Desenvolvido por: Guilherme Henrique & Guilherme Oreste", font=self.FONT_TITULO)
        lb_alunos.pack(pady=20)

    def criar_frame_filme(self):
        self.frame_filme = tk.Frame(self.janela)
        
        self.editando_filme = None

        self.frame_filme.columnconfigure

        # Título
        label_titulo = tk.Label(self.frame_filme, text="Filmes", font=self.FONT_TEXTO)
        label_titulo.grid(column=0, row=0, columnspan=2, pady=20)

        # Linha 1 - Título
        label_titulo_filme = tk.Label(self.frame_filme, text="Título: ", font=self.FONT_TEXTO)
        label_titulo_filme.grid(column=0, row=1, sticky="e", padx=10, pady=5)
        self.entry_titulo = tk.Entry(self.frame_filme, font=self.FONT_TEXTO)
        self.entry_titulo.grid(column=1, row=1, sticky="w", padx=10, pady=5)

        # Linha 2 - Diretor
        label_diretor = tk.Label(self.frame_filme, text="Diretor: ", font=self.FONT_TEXTO)
        label_diretor.grid(column=0, row=2, sticky="e", padx=10, pady=5)
        self.entry_diretor = tk.Entry(self.frame_filme, font=self.FONT_TEXTO)
        self.entry_diretor.grid(column=1, row=2, sticky="w", padx=10, pady=5)

        # Linha 3 - Duração
        label_duracao = tk.Label(self.frame_filme, text="Duração (min): ", font=self.FONT_TEXTO)
        label_duracao.grid(column=0, row=3, sticky="e", padx=10, pady=5)
        self.entry_duracao_minutos = tk.Entry(self.frame_filme, font=self.FONT_TEXTO)
        self.entry_duracao_minutos.grid(column=1, row=3, sticky="w", padx=10, pady=5)

        # Linha 4 - Ano de Lançamento
        label_ano = tk.Label(self.frame_filme, text="Ano de Lançamento: ", font=self.FONT_TEXTO)
        label_ano.grid(column=0, row=4, sticky="e", padx=10, pady=5)
        self.entry_ano_lancamento = tk.Entry(self.frame_filme, font=self.FONT_TEXTO)
        self.entry_ano_lancamento.grid(column=1, row=4, sticky="w", padx=10, pady=5)

        button_editar =  tk.Button(self.frame_filme, text="Editar", font=(self.FONT_TEXTO), command=self.editarFilme)
        button_editar.grid(column=0, row=6, pady=15)

        button_excluir =  tk.Button(self.frame_filme, text="Excluir", font=(self.FONT_TEXTO), command=self.excluirFilme)
        button_excluir.grid(column=1, row=6, pady=15)

        button_atualizar =  tk.Button(self.frame_filme, text="Atualizar", font=(self.FONT_TEXTO), command=self.listarFilmes)
        button_atualizar.grid(column=2, row=6, pady=15)

        button_cadastrar =  tk.Button(self.frame_filme, text="Cadastrar", font=(self.FONT_TEXTO), command=self.cadastrarFilme)
        button_cadastrar.grid(column=3, row=6, pady=15)

        self.listbox_filme = tk.Listbox(self.frame_filme, width=85, height=25)
        self.listbox_filme.grid(column=0, row=5, columnspan=3, padx=10)

        self.listbox_filme.bind('<<ListboxSelect>>', self.preencherlistbox_filme)

        self.listarFilmes()
        
    def criar_frame_cliente(self):
        self.frame_cliente = tk.Frame(self.janela)
        editando_cli = None

        self.frame_cliente.columnconfigure

        label_titulo = tk.Label(self.frame_cliente, text="Clientes", font=(self.FONT_TEXTO)).grid(column=0, row=0, columnspan=3, padx=200)
        label_nome = tk.Label(self.frame_cliente, text="Nome: ", font=(self.FONT_TEXTO)).grid(column=0, row=1)

        self.entry_nome = tk.Entry(self.frame_cliente, font=(self.FONT_TEXTO))
        self.entry_nome.grid(column=1, row=1)

        label_telefone = tk.Label(self.frame_cliente, text="Telefone: ", font=(self.FONT_TEXTO)).grid(column=0, row=2)

        self.entry_telefone = tk.Entry(self.frame_cliente, font=(self.FONT_TEXTO))
        self.entry_telefone.grid(column=1, row=2)

        label_endereco = tk.Label(self.frame_cliente, text="Endereço: ", font=(self.FONT_TEXTO)).grid(column=0, row=3)

        self.entry_endereco = tk.Entry(self.frame_cliente, font=(self.FONT_TEXTO))
        self.entry_endereco.grid(column=1, row=3)

        button_cadastrar =  tk.Button(self.frame_cliente, text="Cadastrar", font=(self.FONT_TEXTO), command=self.cadastrarCliente)
        button_cadastrar.grid(column=0, row=4, pady=30)

        button_editar =  tk.Button(self.frame_cliente, text="Editar", font=(self.FONT_TEXTO), command=self.editarCliente)
        button_editar.grid(column=0, row=6, pady=15)

        button_excluir =  tk.Button(self.frame_cliente, text="Excluir", font=(self.FONT_TEXTO), command=self.excluirCliente)
        button_excluir.grid(column=1, row=6, pady=15)

        button_atualizar =  tk.Button(self.frame_cliente, text="Atualizar", font=(self.FONT_TEXTO), command=self.listarClientes)
        button_atualizar.grid(column=2, row=6, pady=15)

        self.listbox_cli = tk.Listbox(self.frame_cliente, width=85, height=25)
        self.listbox_cli.grid(column=0, row=5, columnspan=3, padx=10)

        self.listbox_cli.bind('<<ListboxSelect>>', self.preencherListbox_Cliente)

    def criar_frame_locacao(self):
        self.frame_locacao = tk.Frame(self.janela)

        label_cliente = tk.Label(self.frame_locacao, text="Cliente:")
        label_cliente.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        self.combobox_cliente = ttk.Combobox(self.frame_locacao, values=[""])
        self.atualizarComboClientes()

        self.combobox_cliente.grid(row=0, column=1, padx=10, pady=10, sticky="we")

        self.combobox_filme = ttk.Combobox(self.frame_locacao, values=[""])
        self.atualizarComboFilme()
        self.combobox_filme.grid(row=1, column=1, padx=10, pady=10, sticky="we")

        button_salvar = tk.Button(self.frame_locacao, text="Salvar", command=self.salvarLocacao)
        button_salvar.grid(row=3, column=0, pady=20)

        self.listbox_locacao = tk.Listbox(self.frame_locacao, width=85, height=25)
        self.listbox_locacao.grid(column=0, row=5, columnspan=3, padx=10)

    def atualizarComboClientes(self):
        self.combobox_cliente["values"] = [f"{cli.id} : : {cli.nome}" for cli in Cliente.select()]
    
    def atualizarComboFilme(self):
        self.combobox_filme["values"] = [f"{filme.id} : : {filme.titulo}" for filme in Filme.select()]

    def mostrar_inicio(self):
        self.frame_inicio.tkraise()
    
    def mostrar_sobre(self):
        self.frame_sobre.tkraise()
    
    def mostrar_cliente(self):
        self.listarClientes()
        self.frame_cliente.tkraise()
    
    def mostrar_filme(self):
        self.listarFilmes()
        self.frame_filme.tkraise()

    def mostrar_locacao(self):
        self.listarLocacao()
        self.frame_locacao.tkraise()

    def listarClientes(self):
        self.listbox_cli.delete(0, tk.END)

        for cliente in Cliente.select():
            print(f"id: {cliente.id}, nome: {cliente.nome}")
            self.listbox_cli.insert(cliente.id, f"{cliente.id} : : {cliente.nome}")

    def cadastrarCliente(self):
        global editando_cli

        nome = (self.entry_nome.get())
        endereco = (self.entry_endereco.get())
        telefone = (self.entry_telefone.get())

        if not nome or not endereco or not telefone:
            messagebox.showerror("ERROR_sans", "É necessário inserir os valores para salvar.")
            return
        
        try:
            Cliente.create(nome = nome, telefone = telefone, endereco = endereco) 
            messagebox.showinfo("3º INFO", f"Deu certo cadastrou o  {nome} .")
            self.atualizarComboClientes()
            self.listarClientes()
            self.entry_nome.delete(0, tk.END)
            self.entry_endereco.delete(0, tk.END)
            self.entry_telefone.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao cadastrar: {e}")
    
    def excluirCliente(self):
        selecionado = self.listbox_cli.curselection()
        if not selecionado:
            messagebox.showwarning("Atenção", "Selecione um cliente para excluir.")
            return
        

        cliente_selecionado = self.listbox_cli.get(selecionado[0])
        cliente_id = int(cliente_selecionado.split(" : : ")[0])

        try:
            cliente = Cliente.get_by_id(cliente_id)
            messagebox.showinfo("é", f"O(A) Cliente '{cliente.nome}' foi excluído(a)!")
            cliente.delete_instance()
            locacoes_deletadas = Locacao.delete().where(Locacao.cliente_id == cliente_id).execute()
            self.listarClientes()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao excluir....: {e}")

    def editarCliente(self):
        global editando_cli

        print(f"estou editando: {editando_cli}")
        if (editando_cli != None):
            try:
                cliente = Cliente.get_by_id(editando_cli)
                novo_nome = (self.entry_nome.get())
                novo_endereco = (self.entry_endereco.get())
                novo_telefone = (self.entry_telefone.get())
                if not novo_nome or not novo_endereco or not novo_telefone:
                    messagebox.showwarning("Atenção", "tem que colocar as coisas")
                    return
                
                cliente.nome = novo_nome
                cliente.endereco = novo_endereco
                cliente.telefone = novo_telefone

                cliente.save()
                messagebox.showinfo("Sucesso", "O cliente foi editado!")
                
                self.listarClientes()
                editando_cli = None
                self.atualizarComboClientes()

            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao editar o cliente: {e}")
        else:
            messagebox.showerror("Erro", f"Selecione um cliente para editar: {e}")

    def preencherListbox_Cliente(self, event):
        global editando_cli
        
        selecionado = self.listbox_cli.curselection()
        if not selecionado:
            return
        
        cliente_selecionado = self.listbox_cli.get(selecionado[0])

        if cliente_selecionado:
            cliente_id = int(cliente_selecionado.split(' : : ')[0])
            cliente = Cliente.get_by_id(cliente_id)

            if (cliente):    
                editando_cli = cliente_id
                self.entry_nome.config(textvariable=(tk.StringVar(value=(cliente.nome))))
                self.entry_telefone.config(textvariable=(tk.StringVar(value=(cliente.telefone))))
                self.entry_endereco.config(textvariable=(tk.StringVar(value=(cliente.endereco))))

    def listarFilmes(self):
        self.listbox_filme.delete(0, tk.END)
        for filme in Filme.select():
            print(f"id: {filme.id}, nome: {filme.titulo}")
            self.listbox_filme.insert(filme.id, f"{filme.id} : : {filme.titulo}")

    def cadastrarFilme(self):
        global editando_filme

        titulo = (self.entry_titulo.get())
        diretor = (self.entry_diretor.get())
        duracao = (self.entry_duracao_minutos.get())
        ano = (self.entry_ano_lancamento.get())

        if not titulo or not diretor or not duracao or not ano:
            messagebox.showerror("ERROR_sans", "É necessário inserir os valores para salvar.")
            return
        
        try:
            Filme.create(titulo = titulo, diretor = diretor, duracao_minutos = duracao, ano_lancamento = ano) 
            messagebox.showinfo("3º INFO", f"Deu certo cadastrou o filme  {titulo} .")
            self.listarFilmes()
            self.entry_titulo.delete(0, tk.END)
            self.entry_diretor.delete(0, tk.END)
            self.entry_duracao_minutos.delete(0, tk.END)
            self.entry_ano_lancamento.delete(0, tk.END)
            self.atualizarComboFilme()            

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao cadastrar o filme: {e}")

    def excluirFilme(self):
        selecionado = self.listbox_filme.curselection()
        if not selecionado:
            messagebox.showwarning("Atenção", "Selecione um filme para excluir.")
            return
        

        filme_selecionado = self.listbox_filme.get(selecionado[0])
        filme_id = filme_selecionado.split(" : : ")[0]
        try:
            filme = Filme.get_by_id(filme_id)
            messagebox.showinfo("é", f"O Filme '{filme.titulo}' foi excluído!")
            filme.delete_instance()
            self.listarFilmes()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao excluir....: {e}")

    def editarFilme(self):
        global editando_filme

        if (editando_filme != None):
            try:
                filme = Filme.get_by_id(editando_filme)
                novo_titulo = (self.entry_titulo.get())
                novo_diretor = (self.entry_diretor.get())
                nova_duracao = (self.entry_duracao_minutos.get())
                novo_ano = (self.entry_ano_lancamento.get())

                if not novo_titulo or not novo_diretor or not nova_duracao or not novo_ano:
                    messagebox.showerror("ERROR_sans", "É necessário inserir os valores para salvar.")
                    return
            
                filme.titulo = novo_titulo
                filme.diretor = novo_diretor
                filme.duracao_minutos = nova_duracao
                filme.ano_lancamento = novo_ano
                filme.save()
                messagebox.showinfo("Sucesso", "O filme foi editado!@")
                
                self.listarFilmes()
                editando_filme = None

                self.atualizarComboFilme()
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao editar o filme >: {e}")
        else:
            messagebox.showerror("Erro", f"Selecione um filme para editar: {e}")

    def preencherlistbox_filme(self, event):
        global editando_filme
        
        selecionado = self.listbox_filme.curselection()
        if not selecionado:
            return
        
        filme_selecionado = self.listbox_filme.get(selecionado[0])

        if filme_selecionado:
            filme_id = int(filme_selecionado.split(' : : ')[0])
            filme = Filme.get_by_id(filme_id)

            if (filme):    
                editando_filme = filme_id
                self.entry_titulo.config(textvariable=(tk.StringVar(value=(filme.titulo))))
                self.entry_diretor.config(textvariable=(tk.StringVar(value=(filme.diretor))))
                self.entry_duracao_minutos.config(textvariable=(tk.StringVar(value=(filme.duracao_minutos))))
                self.entry_ano_lancamento.config(textvariable=(tk.StringVar(value=(filme.ano_lancamento))))
    
    def listarLocacao(self):
        self.listbox_locacao.delete(0, tk.END)
        for locacao in Locacao.select():
            self.listbox_locacao.insert(locacao.id, f"{locacao.id} : : o(a) cliente: {locacao.cliente.nome} alocou o filme: {locacao.filme.titulo}")

    def salvarLocacao(self):
        try:
            cliente_selecionado = self.combobox_cliente.get()
            cliente_id = int(cliente_selecionado.split(" : : ")[0])
            cliente = Cliente.get_by_id(cliente_id)

            filmes_selecionado = self.combobox_filme.get() 
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

    def preencherComboboxLocacao(self):
        clientes = [f"{cli.id} : : {cli.nome}" for cli in Cliente.select()]
        filmes = [f"{filme.id} : : {filme.titulo}" for filme in Filme.select()]

        self.combobox_cliente.config(values=clientes)
        self.combobox_filme = ttk.Combobox(self.frame_locacao, values=filmes)

    def iniciar_aplicacao(self):
        self.frame_inicio.tkraise()
        self.janela.config(menu=self.menubar)
        self.janela.mainloop()

if __name__ == "__main__":
    sistema = Locadora()