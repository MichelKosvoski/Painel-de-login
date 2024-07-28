import tkinter as tk
from tkinter import ttk
import sqlite3
import Intro

# Função para criar o banco de dados e as tabelas
def criar_banco_de_dados():
    conn = sqlite3.connect('sistema.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        endereco TEXT NOT NULL,
        telefone TEXT NOT NULL
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS funcionarios (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        cargo TEXT NOT NULL,
        telefone TEXT NOT NULL
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        quantidade INTEGER NOT NULL,
        preco REAL NOT NULL
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS vendas (
        id INTEGER PRIMARY KEY,
        produto_id INTEGER NOT NULL,
        quantidade INTEGER NOT NULL,
        valor_total REAL NOT NULL,
        data_venda TEXT NOT NULL,
        FOREIGN KEY (produto_id) REFERENCES produtos(id)
    )
    ''')
    
    conn.commit()
    conn.close()

# Função para exibir a tela de área de venda
def mostrar_tela_venda(event=None):
    limpar_tela()
    label = tk.Label(tela_principal, text="Área de Venda", font=("Helvetica", 16))
    label.pack(pady=10)

# Função para exibir a tela de controle de estoque
def mostrar_tela_estoque(event=None):
    limpar_tela()
    label = tk.Label(tela_principal, text="Controle de Estoque", font=("Helvetica", 16))
    label.pack(pady=10)

# Função para exibir a tela de cadastro de estoque
def mostrar_tela_cadastro_estoque(event=None):
    limpar_tela()
    label = tk.Label(tela_principal, text="Cadastro de Estoque", font=("Helvetica", 16))
    label.pack(pady=10)

# Função para exibir a tela de saída de venda
def mostrar_tela_saida_venda(event=None):
    limpar_tela()
    label = tk.Label(tela_principal, text="Saída de Venda", font=("Helvetica", 16))
    label.pack(pady=10)

# Função para exibir a tela de cadastro de clientes
def mostrar_tela_cadastro_cliente(event=None):
    limpar_tela()
    label = tk.Label(tela_principal, text="Cadastro de Clientes", font=("Helvetica", 16))
    label.pack(pady=10)

# Função para exibir a tela de cadastro de funcionários
def mostrar_tela_cadastro_funcionario(event=None):
    limpar_tela()
    label = tk.Label(tela_principal, text="Cadastro de Funcionários", font=("Helvetica", 16))
    label.pack(pady=10)

# Função para limpar a tela
def limpar_tela():
    for widget in tela_principal.winfo_children():
        widget.destroy()

# Criar a janela principal
root = tk.Tk()
root.title("Sistema de Gestão")
root.geometry("800x600")

# Criar um frame principal
tela_principal = tk.Frame(root)
tela_principal.pack(fill=tk.BOTH, expand=True)

# Criar o menu principal
menu_principal = tk.Menu(root)
root.config(menu=menu_principal)

# Adicionar opções ao menu
menu_opcoes = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Opções", menu=menu_opcoes)
menu_opcoes.add_command(label="Área de Venda", command=mostrar_tela_venda, accelerator="Ctrl+D")
menu_opcoes.add_command(label="Controle de Estoque", command=mostrar_tela_estoque, accelerator="Ctrl+E")
menu_opcoes.add_command(label="Cadastro de Estoque", command=mostrar_tela_cadastro_estoque)
menu_opcoes.add_command(label="Saída de Venda", command=mostrar_tela_saida_venda)
menu_opcoes.add_command(label="Cadastro de Clientes", command=mostrar_tela_cadastro_cliente)
menu_opcoes.add_command(label="Cadastro de Funcionários", command=mostrar_tela_cadastro_funcionario)
menu_opcoes.add_separator()
menu_opcoes.add_command(label="Sair", command=root.quit)

# Associar atalhos de teclado
root.bind('<Control-d>', mostrar_tela_venda)

# Criar o banco de dados e as tabelas se não existirem
criar_banco_de_dados()

# Iniciar a aplicação
root.mainloop()