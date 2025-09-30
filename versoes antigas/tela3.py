from código.classes_database import *
from código.classe_logica import *

import tkinter as tk
from tkinter import messagebox, ttk

lista_id = []
editando = [False, -1, -1]

janela = tk.Tk()
janela.title("Exemplo de Combobox")
janela.geometry("650x800")

FONTE = ("Comic Sans MS", 20, "bold")


preencherListBox(listbox)
atualizarLocacao()


janela.mainloop()
