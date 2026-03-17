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