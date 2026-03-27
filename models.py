from database import conectar
import sqlite3

def inserir_usuario(nome, cpf, tel, email, senha, cargo, status):
    conn = sqlite3.connect('loja.db')
    cursor = conn.cursor()

    cursor.execute(""" 
        INSERT INTO usuario (nome, cpf, tel, email, senha, status, cargo)
        VALUES(?,?,?,?,?,?,?)
    """, (nome, cpf, tel, email, senha, status, cargo))

    conn.commit()
    conn.close()


def validar_usuario(email, senha):
    conn = sqlite3.connect('loja.db')
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM usuario
    WHERE email = ? AND senha = ? """, (email, senha))

    usuario = cursor.fetchone()
    conn.close()

    return usuario

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