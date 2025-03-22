from flask import render_template, request, redirect, session, flash, url_for, jsonify
from models import models
from main import app, conexao

import mysql
import typing

torneios = []
torneio_1 = models.Torneio('Rolang Rools', 2025)
torneio_2 = models.Torneio('Champions', 2024)
torneio_3 = models.Torneio('Torneio do Círio', 2023)
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
        novo_torneio = models.Torneio(nome,ano)
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
    
    cnx = mysql.connector.connect(host="127.0.0.1",
                                    port=3306,
                                    database="db_bilhar_champ",
                                    user="root",
                                    password="123")
    cursor = cnx.cursor()    
    cursor.execute("SELECT id_jogador, nome, data_nascimento, cpf, cep FROM jogador")
    
    jogadores_recuperados = cursor.fetchall()
    
    if len(jogadores_recuperados) > 0:
        global jogadores
        jogadores = []
        for jog in jogadores_recuperados:
            jogador = models.Jogador()
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

    jogador = models.Jogador(nome = nome, data_nascimento = data_nascimento, cpf = cpf, cep = cep)
    
    # cadastrar jogador na base
    # cnx: typing[MySQLConnection] = conexao
    cursor = conexao.cursor()
    
    insert_jogador = "INSERT INTO jogador (nome, data_nascimento, cpf, cep) VALUES (%s, %s, %s, %s)"
    
    cursor.execute(insert_jogador,
               (jogador.nome, jogador.data_nascimento, jogador.cpf, jogador.cep))
    conexao.commit()
    conexao.close()
    
    return redirect('/jogador')

    
@app.route("/detalhar-jogador")
def detalhar_jogador():
    return render_template('detalhe-jogador.html')


@app.route("/excluir-jogador", methods = ['POST',])
def excluir_jogador():
    id_jogador =  tuple(request.form.get('id_jogador')) 
    
    cnx = models
    cursor = cnx.cursor()
    
    deletar_jogador = "DELETE FROM jogador WHERE id_jogador = (%s)"
    
    cursor.execute(deletar_jogador, id_jogador)
    cnx.commit()
    
    return jsonify({'redirect': url_for('jogador')})

@app.route("/logout")
def logout():   
    session.clear()
    flash('O usuário não está logado.')
    return redirect('/index')


@app.route("/editar-jogador", methods=['GET',])
def editarJogador():
    form = request.form
    return render_template('editar-jogador-form.html', form=form)
    

@app.route("/editar-jogador-form", methods=['POST',])
def editarJogadorForm():
    form = request.form
    if request.method == 'POST':
        jogador = models.Jogador(form.nome.data, form.data_nascimento.data, form.cpf.data, form.cep.data)
        cnx = conexao
        # atualizar jogador
        return redirect(url_for('jogador'))