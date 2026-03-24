import tkinter as tk
from tkinter import messagebox
from models import adicionar_produto

class adproduto(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Adicionar Produto", font=("Arial", 16)).pack(pady=10)


        tk.Label(self, text="Nome:").pack()
        self.nome_entry = tk.Entry(self)
        self.nome_entry.pack()

        tk.Label(self, text="Descrição:").pack()
        self.descricao_entry = tk.Entry(self)
        self.descricao_entry.pack()

        tk.Label(self, text="Preço:").pack()
        self.preco_entry = tk.Entry(self)
        self.preco_entry.pack()

        tk.Label(self, text="Estoque:").pack()
        self.estoque_entry = tk.Entry(self)
        self.estoque_entry.pack()

        tk.Button(self, text="Adicionar", width=20, command=self.adicionar_produto).pack(pady=10)
        tk.Button(self, text="Voltar", width=20,
                  command=lambda: controller.mostrar_frame("HP")).pack(pady=5)

    def adicionar_produto(self):
        nome = self.nome_entry.get()
        descricao = self.descricao_entry.get()
        try:
            preco = float(self.preco_entry.get())
            estoque = int(self.estoque_entry.get())
        except ValueError:
            messagebox.showerror("Erro", "Preço e Estoque devem ser números!")
            return
        adicionar_produto(nome, descricao, preco, estoque)

        messagebox.showinfo("Sucesso", f"Produto '{nome}' cadastrado!")

        self.nome_entry.delete(0, tk.END)
        self.descricao_entry.delete(0, tk.END)
        self.preco_entry.delete(0, tk.END)
        self.estoque_entry.delete(0, tk.END)