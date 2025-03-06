from flask import Flask, render_template, request, redirect, session, flash, url_for, jsonify
import json
import mysql.connector
from typing import Type


app = Flask(__name__)
app.secret_key = 'teste'

class Jogador():
    def __init__(self, id_jogador = None, nome = None, data_nascimento = None, cpf = None, cep = None):
        self.id_jogador = id_jogador
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.cep = cep
        
    def validarCpf(cpf: str) -> bool:
        pass

    def validarCep(cep:str) -> bool:
        pass
    
    def to_dict(self):
        return {
            "nome": self.nome,
            "data_nascimento": self.data_nascimento,
            "cpf": self.cpf,
            "cep": self.cep
        }
        
    def convert_to_objetc(self, jogador: tuple):
        return Jogador(jogador[0], jogador[1], jogador[2], jogador[3], jogador[4])

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
jogadores: list = []

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
    
    cnx = load_conection()
    cursor = cnx.cursor()    
    cursor.execute("SELECT id_jogador, nome, data_nascimento, cpf, cep FROM jogador")
    
    jogadores_recuperados = cursor.fetchall()
    
    if len(jogadores_recuperados) > 0:
        global jogadores
        for jog in jogadores_recuperados:
            jogador = Jogador()
            jogador_convertido = jogador.convert_to_objetc(jog)
            jogadores.append(jogador_convertido)
    else:
        jogadores = []
        
    return render_template('jogador.html', jogadores = jogadores)

@app.route("/cadastrar_jogador", methods = ['POST'])
def cadastrar_jogador():
    global jogadores
    nome = request.form['nome']
    data_nascimento = request.form['data_nascimento']
    cpf = request.form['cpf']
    cep = request.form['cep']

    jogador = Jogador(nome = nome, data_nascimento = data_nascimento, cpf = cpf, cep = cep)
    
    # cadastrar jogador na base
    cnx = load_conection()
    cursor = cnx.cursor()
    
    insert_jogador = "INSERT INTO jogador (nome, data_nascimento, cpf, cep) VALUES (%s, %s, %s, %s)"
    
    cursor.execute(insert_jogador,
               (jogador.nome, jogador.data_nascimento, jogador.cpf, jogador.cep))
    cnx.commit()
    
    jogadores.append(jogador)
    cnx.close()
    
    return render_template('jogador.html', jogadores=jogadores)

    
@app.route("/detalhar-jogador")
def detalhar_jogador():
    return render_template('detalhe-jogador.html')


@app.route("/excluir-jogador", methods = ['POST',])
def excluir_jogador():
    id_jogador =  int(request.form.get('id_jogador')) 

    #deletar da base de dados
    
    for index, jog in enumerate(jogadores):
        if jog.get('nome') == jogador.get('nome'):
            jogadores.pop(index)

    return jsonify({'jogadores': jogadores, 'redirect': url_for('jogador')})

@app.route("/logout")
def logout():   
    session.clear()
    flash('O usuário não está logado.')
    return redirect('/index')


def load_conection():
    cnx = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        database="db_bilhar_champ",
        user="root",
        password="123",
    )
    
    return cnx


if __name__ == '__main__':
    app.run(debug=True)