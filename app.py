from flask import Flask, render_template, request, redirect
from database import criar_tabelas
from models import listar_produtos, deletar_produtos

app = Flask(__name__)

# cria as tabelas ao iniciar
criar_tabelas()

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/produtos')
def produtos():
    filtro = request.args.get('filtro')

    produtos = listar_produtos()

    if filtro:
        produtos = [p for p in produtos if filtro.lower() in p[1].lower()]

    return render_template('produtos.html', produtos=produtos)


@app.route('/deletar/<int:id>')
def deletar(id):
    deletar_produtos(id)
    return redirect('/produtos')


if __name__ == '__main__':
    app.run(debug=True)