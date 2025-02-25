from flask import Flask, render_template, request

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

@app.route("/cadastrar-torneio", methods = ['POST'])
def cadastrar_torneio():
    request.method == 'POST'
    nome = request.get_data('nome')
    return f"Nome preenchido {nome}"

if __name__ == '__main__':
    app.run(debug=True)