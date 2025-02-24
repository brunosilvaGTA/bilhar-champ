
from flask import Flask
from flask import render_template
from flask import url_for
from flask import request

app = Flask(__name__)



@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/home")
def app_home():
    css_url = url_for('static', filename='css/styles.css')
    return render_template('home.html', css_url=css_url)


@app.route("/torneio")
def torneio():
    return render_template('form.html')

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    if request.method == 'POST':
        nome = request.form.get('nome')
        
        return f"Received: nome - {nome}"
    
if __name__ == '__main__':
    app.run(debug=True)