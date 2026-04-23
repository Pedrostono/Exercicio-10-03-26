import os
from database import conectar
import sqlite3
import hashlib
import re
from datetime import datetime, timedelta

def limpar_texto(texto):
    return re.sub(r'<.*?>', '', texto)

def hash_senha(senha):
    salt = os.urandom(16)
    hash_obj = hashlib.sha256(salt + senha.encode())
    return salt.hex() + hash_obj.hexdigest()

def verificar_senha(senha, senha_salva):
    salt = bytes.fromhex(senha_salva[:32])
    hash_salvo = senha_salva[32:]

    hash_obj = hashlib.sha256(salt + senha.encode())
    return hash_obj.hexdigest() == hash_salvo

def cpf_existe(cpf):
    conn = sqlite3.connect('loja.db')
    cursor = conn.cursor()

    cursor.execute("SELECT 1 FROM usuario WHERE cpf = ?", (cpf,))
    existe = cursor.fetchone()

    conn.close()
    return existe is not None


def inserir_usuario(nome, cpf, tel, email, senha, status, cargo):
    conn = sqlite3.connect('loja.db')
    cursor = conn.cursor()

    if cpf_existe(cpf):
        conn.close()
        return False

    senha_hash = hash_senha(senha)

    cursor.execute(""" 
        INSERT INTO usuario (nome, cpf, tel, email, senha, status, cargo)
        VALUES(?,?,?,?,?,?,?)
    """, (nome, cpf, tel, email, senha_hash, status, cargo))

    conn.commit()
    conn.close()
    return True

def registrar(usuario):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO relatorio (usuario_id, nome_usuario)
    VALUES (?, ?)
    """, (usuario["id"], usuario["nome"]))

    conn.commit()
    conn.close()

def listar_relatorios():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM relatorio ORDER BY id DESC")
    dados = cursor.fetchall()

    conn.close()
    return dados

def adicionar_produto(nome, descricao, preco, estoque):
    conn = sqlite3.connect('loja.db')
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO produtos (nome, descricao, preco, estoque)
    VALUES (?, ?, ?, ?)
    """, (nome, descricao, preco, estoque))

    conn.commit()
    conn.close()

def validar_usuario(email, senha):
    conn = sqlite3.connect('loja.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuario WHERE email = ?", (email,))
    usuario = cursor.fetchone()

    conn.close()

    if usuario and verificar_senha(senha, usuario["senha"]):
        registrar(usuario)
        return usuario

    return None


def listar_produtos():
    conn = conectar()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()

    conn.close()
    return produtos

def deletar_produtos(id):
    conn = sqlite3.connect('loja.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM produtos WHERE id = ?", (id,))

    conn.commit()
    conn.close()

def verificar_produto(id):
    conn = sqlite3.connect('loja.db')
    cursor = conn.cursor()

    cursor.execute("SELECT 1 FROM produtos WHERE id = ?", (id,))
    produto = cursor.fetchone()

    conn.close()
    return produto is not None

def listar_user():
    conn = conectar()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuario")
    usuarios = cursor.fetchall()
    
    conn.close()
    return usuarios


def deletar_users(id):
    conn = sqlite3.connect('loja.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM usuario WHERE id = ?", (id,))

    conn.commit()
    conn.close()

def produto_reservado(produto_id):
    """Verifica se um produto está reservado no momento."""
    conn = conectar()
    cursor = conn.cursor()

    agora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    cursor.execute("""
        SELECT * FROM reservas
        WHERE produto_id = ? AND expira_em > ?
    """, (produto_id, agora))

    reserva = cursor.fetchone()
    conn.close()
    return reserva  # Retorna a reserva se existir, None se estiver livre

def criar_reserva(produto_id, usuario_id, minutos=15):
    """Cria uma reserva para o produto, se ele estiver livre."""
    if produto_reservado(produto_id):
        return False  # Já está reservado

    conn = conectar()
    cursor = conn.cursor()

    agora = datetime.now()
    expira = agora + timedelta(minutes=minutos)

    cursor.execute("""
        INSERT INTO reservas (produto_id, usuario_id, expira_em)
        VALUES (?, ?, ?)
    """, (produto_id, usuario_id, expira.strftime('%Y-%m-%d %H:%M:%S')))

    conn.commit()
    conn.close()
    return True

def cancelar_reserva(produto_id, usuario_id):
    """Cancela a reserva de um produto feita pelo usuário."""
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM reservas
        WHERE produto_id = ? AND usuario_id = ?
    """, (produto_id, usuario_id))

    conn.commit()
    conn.close()