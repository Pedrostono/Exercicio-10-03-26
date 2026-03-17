from database import criar_tabelas
from models import adicionar_produto, listar_produtos

def menu():
    while True:
        print("\n--- LOJA VIRTUAL ---")
        print("1 - Adicionar produto")
        print("2 - Listar produtos")
        print("0 - Sair")

        op = input("Escolha: ")

        if op == "1":
            nome = input("Nome: ")
            descricao = input("Descrição: ")
            preco = float(input("Preço: "))
            estoque = int(input("Estoque: "))

            adicionar_produto(nome, descricao, preco, estoque)
            print("Produto cadastrado!")

        elif op == "2":
            produtos = listar_produtos()

            for p in produtos:
                print(p)

        elif op == "0":
            break


if __name__ == "__main__":
    criar_tabelas()
    menu()