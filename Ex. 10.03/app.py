import tkinter as tk
from home import HP
from adproduto import adproduto
from listar import listagem
from database import criar_tabelas
from deletar import delproduto
from models import adicionar_produto, listar_produtos, deletar_produtos, verificar_produto

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("trocinho")
        self.geometry("400x300")

        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        self.frames = {}

        for F in (HP, adproduto, listagem, delproduto):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.mostrar_frame("HP")

    def mostrar_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


if __name__ == "__main__":
    app = App()
    app.mainloop() 