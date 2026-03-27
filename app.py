from flask import Flask, render_template, request, redirect, session
from database import criar_tabelas
from models import listar_produtos, deletar_produtos, inserir_usuario, validar_usuario, adicionar_produto

app = Flask(__name__)
app.secret_key = "angeleyes"

criar_tabelas()

@app.route('/', methods=['GET','POST'])
def login():
    if request.method == "POST":
        email = request.form.get('emailinp')
        senha = request.form.get('senhainp')
    
        usuario = validar_usuario(email,senha)
        if usuario:
            session['usuario_id'] = usuario[0]
            return redirect('/home')
        else:
            return "Email ou senha incorretos!"


    return render_template('login.html')

@app.route('/home')
def home():
    if 'usuario_id' not in session:
        return redirect('/')
    return render_template('home.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == "POST":
        nome = request.form.get('nomeinp')
        tel = request.form.get('telinp')
        cpf = request.form.get('cpfinp')
        email = request.form.get('emailinp')
        senha = request.form.get('senhainp')
        status = request.form.get('status')
        cargo = request.form.get('cargoinp')

        status = int(status) if status else None
        inserir_usuario(nome, tel, cpf, email, senha, status, cargo)

        return redirect('/')

    return render_template('cadastro.html')

@app.route('/produtos')
def produtos():
    if 'usuario_id' not in session:
        return redirect('/')
    filtro = request.args.get('filtro')

    produtos = listar_produtos()

    if filtro:
        produtos = [p for p in produtos if filtro.lower() in p[1].lower()]

    return render_template('produtos.html', produtos=produtos)


@app.route('/deletar/<int:id>')
def deletar(id):
    if 'usuario_id' not in session:
        return redirect('/')
    deletar_produtos(id)
    return redirect('/produtos')

@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    if 'usuario_id' not in session:
        return redirect('/')
    
    msg = None
    if request.method == "POST":
        nome = request.form.get('prodnome')
        descricao = request.form.get('proddescricao')
        valor = request.form.get('prodvalor')
        estoque = request.form.get('prodestoque')
        adicionar_produto (nome, descricao, valor, estoque)

        valor = float(valor)
        estoque = int(estoque)

        msg = f"Produto '{nome}' adicionado com sucesso!"
    return render_template('adicionar.html', msg=msg)


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)