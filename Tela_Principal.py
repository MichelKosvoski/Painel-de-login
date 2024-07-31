import tkinter as tk
from tkinter import messagebox
import Intro

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Gestão")
        self.geometry("800x600")

        # Menu principal
        menu = tk.Menu(self)
        self.config(menu=menu)

        # Menu Estoque
        estoque_menu = tk.Menu(menu)
        menu.add_cascade(label="Estoque", menu=estoque_menu)
        estoque_menu.add_command(label="Controle de Estoque", command=self.controle_estoque)

        # Menu Venda
        venda_menu = tk.Menu(menu)
        menu.add_cascade(label="Venda", menu=venda_menu)
        venda_menu.add_command(label="Área de Venda", command=self.area_venda)

        # Menu Cliente
        cliente_menu = tk.Menu(menu)
        menu.add_cascade(label="Cliente", menu=cliente_menu)
        cliente_menu.add_command(label="Cadastro de Cliente", command=self.cadastro_cliente)

    def controle_estoque(self):
        # Função para controle de estoque
        messagebox.showinfo("Controle de Estoque", "Controle de Estoque selecionado.")

    def area_venda(self):
        # Função para área de venda
        messagebox.showinfo("Área de Venda", "Área de Venda selecionada.")

    def cadastro_cliente(self):
        # Função para cadastro de cliente
        messagebox.showinfo("Cadastro de Cliente", "Cadastro de Cliente selecionado.")

if __name__ == "__main__":
    app = App()
    app.mainloop()
        

