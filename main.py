from flask import Flask, render_template, request, redirect, session, flash, url_for, jsonify

app = Flask(__name__)
app.secret_key = 'teste'

class Jogador():
    def __init__(self, nome, data_nascimento, cpf, cep):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.cep = cep
    def validarCpf(cpf: str) -> bool:
        pass

    def validarCep(cep:str) -> bool:
        pass

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
jogadores = []

@app.route("/")
def index():
    #session['usuario'] = None
    return render_template('lista-torneio.html', lista = torneios)

@app.route("/torneio")
def torneio():

    if 'usuario' not in session or session['usuario'] == None:
        return redirect('/login?novo-torneio=torneio')
    return render_template('torneio.html')

@app.route("/cadastrar-torneio", methods = ['POST'])
def cadastrar_torneio():
    if request.method == 'POST':
        nome = request.form['nome']
        ano = request.form['ano']
        novo_torneio = Torneio(nome,ano)
        torneios.append(novo_torneio)
        
    return redirect(url_for('index'))

@app.route('/login')
def login():
    novo_torneio = request.args.get('novo-torneio')
    return render_template('login.html', novo_torneio=url_for('torneio'))

@app.route('/autenticar', methods = ['POST'])
def autenticar():
    usuario = request.form['usuario']
    senha = request.form['senha']
    novo_torneio = request.form['novo_torneio']

    session['usuario'] = usuario

    if 'teste' == session['usuario']:
        flash('Usuário está logado!')
        return redirect(novo_torneio)
    else:
        session['usuario'] = None
        flash('Usuário não está logado!')
        return redirect(url_for('login'))
    
@app.route("/jogador")
def jogador():
    return render_template('jogador.html', jogadores = jogadores)

@app.route("/cadastrar_jogador", methods = ['POST'])
def cadastrar_jogador():
    nome = request.form['nome']
    data_nascimento = request.form['data_nascimento']
    cpf = request.form['cpf']
    cep = request.form['cep']

    jogador = Jogador(nome = nome, data_nascimento = data_nascimento, cpf = cpf, cep = cep)
    jogadores.append(jogador)
    return render_template('jogador.html', jogadores = jogadores)
    
@app.route("/detalhar-jogador")
def detalhar_jogador():
    return render_template('detalhe-jogador.html')

@app.route("/excluir-jogador", methods = ['POST',])
def excluir_jogador():
    jogador_nome = request.form['nome'] 
    for index, jog in enumerate(jogadores):
        if jog.nome == jogador_nome:
            jogadores.pop(index)

    flash(f'O jogador {jogador_nome} foi removido!')
    return jsonify(status="success")

@app.route("/logout")
def logout():   
    session.clear()
    flash('O usuário não está logado.')
    return redirect('/index')

if __name__ == '__main__':
    app.run(debug=True)