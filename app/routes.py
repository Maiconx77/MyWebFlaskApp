# app/routes.py
from app import app
from flask import render_template

# Rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html', title="Página Inicial")

# app/routes.py
from flask import request, redirect, url_for, flash

@app.route('/saudacao/<nome>')
def saudacao(nome):
    return f'Olá, {nome}!'

@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        nome = request.form['nome']
        return redirect(url_for('saudacao', nome=nome))
    return '''
        <form method="POST">
            <label for="nome">Seu nome:</label>
            <input type="text" id="nome" name="nome" required>
            <button type="submit">Enviar</button>
        </form>
    '''