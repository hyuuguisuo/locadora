from datetime import date, timedelta
import tkinter as tk
from tkinter import messagebox, ttk

from código.classes_database import Cliente, Filme, Locacao

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


janela = tk.Tk()
janela.title("Exemplo de Combobox")
janela.geometry("450x300")

# Criar um label para cliente
label_cliente = tk.Label(janela, text="Cliente:")
label_cliente.grid(row=0, column=0, padx=10, pady=10, sticky="e")

clientes = [f"{cli.id} : : {cli.nome}" for cli in Cliente.select()]

combobox_cliente = ttk.Combobox(janela, values=clientes)
combobox_cliente.grid(row=0, column=1, padx=10, pady=10, sticky="we")


filmes = [f"{filme.id} : : {filme.titulo}" for filme in Filme.select()]

combobox_filme = ttk.Combobox(janela, values=filmes)
combobox_filme.grid(row=1, column=1, padx=10, pady=10, sticky="we")


# Botões para "salvar"
button_salvar = tk.Button(janela, text="Salvar", command=salvarLocacao)
button_salvar.grid(row=3, column=0, pady=20)

# Roda a janela
janela.mainloop()