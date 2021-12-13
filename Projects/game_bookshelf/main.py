from flask import Flask, render_template, request, redirect, session, flash, url_for

app = Flask(__name__)
app.secret_key = 'testecomseguranca'


# # trecho da app
# app.run(host='0.0.0.0', port=8080)

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


class Usuario:
    def __init__(self, id, nome, senha):
        self.id = id
        self.nome = nome
        self.senha = senha


jogo1 = Jogo('Super Mario', 'Aventura', 'Super Nintendo')
jogo2 = Jogo('Need for Speed', 'Corrida', 'Play Staiton')
jogo3 = Jogo('Fifa2030', 'Esporte', 'Play Staiton')
lista_de_jogos = [jogo1, jogo2, jogo3]

usuario1 = Usuario('cristian', 'Cristian S. S.', '1234')
usuario2 = Usuario('joao', 'Joao P. D.', '4321')
usuario3 = Usuario('marcos', 'Marcos R. T.', '9876')
usuarios = {usuario1.id: usuario1,
            usuario2.id: usuario2,
            usuario3.id: usuario3}


@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista_de_jogos)


@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo='Novo Jogo')


@app.route('/criar', methods=['POST', ])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    novo_jogo = Jogo(nome, categoria, console)
    lista_de_jogos.append(novo_jogo)
    return redirect(url_for('index'))


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)


@app.route('/autenticar', methods=['POST', ])
def autenticar():
    user = request.form['usuario']
    if user in usuarios:
        user = usuarios[user]
        password = request.form['senha']
        if user.senha == password:
            session['usuario_logado'] = user.id
            flash(user.nome + ' logou com sucesso')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else:
        flash('Senha incorreta, tente novamente!')
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuáro logado!')
    return redirect(url_for('index'))


app.run(debug=True)
