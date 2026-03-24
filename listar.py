import tkinter as tk
from models import listar_produtos

class listagem(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Lista de Produtos", font=("Arial", 16)).pack(pady=10)

        tk.Button(self, text="Atualizar Lista", width=20, command=self.atualizar).pack(pady=5)
        tk.Button(self, text="Voltar", width=20, command=lambda: controller.mostrar_frame("HP")).pack(pady=5)

        self.labels_produtos = []

        self.atualizar()

    def atualizar(self):

        for lbl in self.labels_produtos:
            lbl.destroy()
        self.labels_produtos.clear()

        produtos = listar_produtos()
        if not produtos:
            lbl = tk.Label(self, text="Nenhum produto cadastrado.")
            lbl.pack()
            self.labels_produtos.append(lbl)
        else:
            for p in produtos:
                texto = f"ID: {p[0]} | Nome: {p[1]} | Descrição: {p[2]} | Preço: {p[3]} | Estoque: {p[4]}"
                lbl = tk.Label(self, text=texto, anchor="w")
                lbl.pack(fill="x")
                self.labels_produtos.append(lbl)