from flask import Flask

app = Flask(__name__)
app.secret_key = 'teste'
        
app.config.from_pyfile('config.py')

conexao = app.config['DB_MYSQL_CONFIG']

from views import *

if __name__ == '__main__':
    app.run(debug=True)