import tkinter as tk

class HP(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Bem-vindo").pack(pady=20)
        tk.Button(self, text="Adicionar Produto", width=20, command=lambda: controller.mostrar_frame("adproduto")).pack(pady=20)
        tk.Button(self, text="Lista de produtos", width=20, command=lambda: controller.mostrar_frame("listagem")).pack(pady=20)
        tk.Button(self, text="Deletar produto", width=20, command=lambda: controller.mostrar_frame("delproduto")).pack(pady=20)


if __name__ == "__main__":
    app = App()
    app.mainloop()