import tkinter as tk
from tkinter import messagebox
from models import deletar_produtos, verificar_produto

class delproduto(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Deletar Produto", font=("Arial", 16)).pack(pady=10)

        tk.Label(self, text="Digite o ID do produto:").pack(pady=5)
        self.id_entry = tk.Entry(self)
        self.id_entry.pack(pady=5)

        tk.Button(self, text="Deletar Produto", width=20, command=self.deletar_produto).pack(pady=10)
        tk.Button(self, text="Voltar", width=20,
                  command=lambda: controller.mostrar_frame("HP")).pack(pady=5)

    def deletar_produto(self):
        id_text = self.id_entry.get()
        if not id_text.isdigit():
            messagebox.showerror("Erro", "ID deve ser um número!")
            return

        id_produto = int(id_text)

        if verificar_produto(id_produto):
            deletar_produtos(id_produto)
            messagebox.showinfo("Sucesso", f"Produto com ID {id_produto} deletado!")
            self.id_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Erro", "Produto não encontrado!")