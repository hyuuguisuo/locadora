from datetime import date, timedelta
import tkinter as tk
from tkinter import messagebox, ttk
# Importa as classes do Peewee
from código.classes_database import Cliente, Filme, Locacao

# Método para salvar no banco de dados
def salvar_protocolo():
    try:
        # Pega o cliente selecionado no combobox
        cliente_selecionado = combobox_cliente.get() # get pega o texto e .current() a posição
        cliente_id = int(cliente_selecionado.split('(')[-1].strip(')')) # 1 guilherme
        cliente = Cliente.get_by_id(cliente_id)

        filmes_selecionado = combobox_filme.get() 
        filme_id = int(filmes_selecionado.split('(')[-1].strip(')')) # 1 guilherme
        filme = Cliente.get_by_id(filme_id)

        dt_locacao_2 = date.today()
    
        dias_locacao = 14

        dt_devolucao_2 = dt_locacao_2 + timedelta(days=dias_locacao)


        # Cria um novo protocolo e salva no banco de dados
        nova_locacao = Locacao.create(
            cliente=cliente_id,
            filme=filme_id,
            dt_locacao = dt_locacao_2,
            dt_devolucao = dt_devolucao_2,
            valor = 20,
            devolvido=False
        )
        messagebox.showinfo("Sucesso", f"Protocolo {nova_locacao.id} salvo com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao salvar protocolo: {e}")


# Botão para selecionar o cliente com ID 2 no combobox
def selecionar_cliente_id_2():
    # Faz um loop na lista de clientes para encontrar o que tem ID 2
    for i, cliente in enumerate(clientes):
        if cliente.endswith("(2)"):
            combobox_cliente.current(i)
            break   

    # Faz um loop na lista de tipos de protocolo para encontrar o que tem ID 2
    for i, filme in enumerate(filmes):
        if filme.endswith("(2)"):
            combobox_filme.current(i)
            break


# Cria a janela principal com título e tamanho
janela = tk.Tk()
janela.title("Exemplo de Combobox")
janela.geometry("450x300")

# Criar um label para cliente
label_cliente = tk.Label(janela, text="Cliente:")
label_cliente.grid(row=0, column=0, padx=10, pady=10, sticky="e")

clientes = [f"{cli.nome} ({cli.id})" for cli in Cliente.select()]
combobox_cliente = ttk.Combobox(janela, values=clientes)
combobox_cliente.grid(row=0, column=1, padx=10, pady=10, sticky="we")

filmes = [f"{filme.titulo} ({filme.id})" for filme in Filme.select()]
combobox_filme = ttk.Combobox(janela, values=filmes)
combobox_filme.grid(row=1, column=1, padx=10, pady=10, sticky="we")


# Botões para "salvar"
button_salvar = tk.Button(janela, text="Salvar", command=salvar_protocolo)
button_salvar.grid(row=3, column=0, pady=20)

# Botão para selecionar o cliente com ID 2
button_selecionar_id_2 = tk.Button(janela, text="cliente ID 2", command=selecionar_cliente_id_2)
button_selecionar_id_2.grid(row=3, column=1, pady=10)

# Roda a janela
janela.mainloop()