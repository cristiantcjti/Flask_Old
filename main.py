from flask import Flask, render_template, request, redirect

app = Flask(__name__)


# # trecho da app
# app.run(host='0.0.0.0', port=8080)

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


jogo1 = Jogo('Super Mario', 'Aventura', 'Super Nintendo')
jogo2 = Jogo('Need for Speed', 'Corrida', 'Play Staiton')
jogo3 = Jogo('Fifa2030', 'Esporte', 'Play Staiton')
lista_de_jogos = [jogo1, jogo2, jogo3]


@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista_de_jogos)


@app.route('/novo')
def novo_jogo():
    return render_template('novo_jogo.html', titulo='Novo Jogo')


@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    novo_jogo = Jogo(nome, categoria, console)
    lista_de_jogos.append(novo_jogo)
    return redirect('/')

app.run(debug=True)
