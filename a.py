import tkinter as tk

def pegar_selecao():
    selecao = listbox.curselection()
    if selecao:  # se algum item estiver selecionado
        indice = selecao[0]     # Posição do item na Listbox
        texto = listbox.get(indice)  # Texto mostrado naquele item
        print(f"Selecionado: {texto}")
    else:
        print("Nenhum item selecionado")

def ao_selecionar(event):
    selecao = listbox.curselection()
    if selecao:
        indice = selecao[0]
        texto = listbox.get(indice)
        print(f"Selecionou: {texto}")


janela = tk.Tk()
listbox = tk.Listbox(janela, width=30, height=10)
listbox.pack()  

# Você pode chamar essa função por um botão:
botao = tk.Button(janela, text="Ver selecionado", command=pegar_selecao)
botao.pack()

produtos = ["Caderno", "Caneta", "Lápis"]

for produto in produtos:
    listbox.insert(tk.END, produto)

janela.mainloop()