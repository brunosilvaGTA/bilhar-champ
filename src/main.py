
from flask import Flask
from flask import render_template
from flask import url_for
from flask import request


app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('base.html')


@app.route("/home")
def app_home():
    return render_template('child.html')


@app.route("/torneio")
def torneio():
    return render_template('torneio.html')


@app.route("/cadastrar-torneio", methods=['POST'])
def cadastrar_torneio():
    if request.method == 'POST':
        nome = request.get_data('nome')
        qtd_participantes = request.get_data('qtdParticipantes')

        return f"Nome preenchido {nome}, Qtd_participantes: {qtd_participantes}"




if __name__=="__main__":
    app.run(debug=True)