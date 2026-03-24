from database import conectar

def adicionar_produto(nome, descricao, preco, estoque):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO produtos (nome, descricao, preco, estoque)
    VALUES (?, ?, ?, ?)
    """, (nome, descricao, preco, estoque))

    conn.commit()
    conn.close()


def listar_produtos():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()

    conn.close()
    return produtos

def deletar_produtos(id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM produtos WHERE id = ?", (id,))

    conn.commit()
    conn.close()

def verificar_produto(id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute ("SELECT * FROM produtos where id = ?", (id,))
    produto = cursor.fetchone()

    if produto is None:
        print("Esse produto não existe")
        return False
    else:
        return True