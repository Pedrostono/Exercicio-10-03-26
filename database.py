import sqlite3

DB_NAME = "loja.db"



def conectar():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn




def criar_tabelas():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        descricao TEXT,
        preco REAL NOT NULL,
        estoque INTEGER NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS carrinho (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        produto_id INTEGER,
        quantidade INTEGER,
        FOREIGN KEY(produto_id) REFERENCES produtos(id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuario (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL CHECK (nome LIKE '% %'),
        cpf TEXT UNIQUE NOT NULL,
        email TEXT NOT NULL,
        tel TEXT,
        senha TEXT NOT NULL,
        status INTEGER DEFAULT 1,
        cargo TEXT
    )
    """)

    cursor.execute("""
CREATE TABLE IF NOT EXISTS relatorio (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER NOT NULL,
    nome_usuario TEXT NOT NULL,
    data DATE DEFAULT (DATE('now','localtime')),
    hora TIME DEFAULT (TIME('now','localtime')),
    FOREIGN KEY(usuario_id) REFERENCES usuario(id)
)
""")
    
    cursor.execute("""
CREATE TABLE IF NOT EXISTS reservas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    produto_id INTEGER NOT NULL,
    usuario_id INTEGER NOT NULL,
    criado_em DATETIME DEFAULT (DATETIME('now', 'localtime')),
    expira_em DATETIME NOT NULL,
    FOREIGN KEY(produto_id) REFERENCES produtos(id),
    FOREIGN KEY(usuario_id) REFERENCES usuario(id)
)
""")

    conn.commit()
    conn.close()