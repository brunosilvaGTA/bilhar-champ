from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'teste'
class Torneio():
    def __init__(self, nome, ano):
        self.nome = nome
        self.ano = ano


torneios = []
torneio_1 = Torneio('Rolang Rools', 2025)
torneio_2 = Torneio('Champions', 2024)
torneio_3 = Torneio('Torneio do Círio', 2023)
torneios.append(torneio_1)
torneios.append(torneio_2)
torneios.append(torneio_3)

@app.route("/")
def index():
    #session['usuario'] = None
    return render_template('lista-torneio.html', lista = torneios)

@app.route("/torneio")
def torneio():

    if session and session['usuario'] == 'teste':
        flash('Usuário está logado')
        return render_template('torneio.html')
    else:
        flash('Usuário não está logado!')
        return redirect('/')

@app.route("/cadastrar-torneio", methods = ['POST'])
def cadastrar_torneio():
    if request.method == 'POST':
        nome = request.form['nome']
        ano = request.form['ano']
        novo_torneio = Torneio(nome,ano)
        torneios.append(novo_torneio)

        
    return redirect('/')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods = ['POST'])
def autenticar():
    usuario = request.form['usuario']
    senha = request.form['senha']

    session['usuario'] = usuario

    if 'teste' == session['usuario']:
        flash('Usuário está logado!')
        return redirect('/')
    else:
        session['usuario'] = None
        flash('Usuário não está logado!')
        return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)